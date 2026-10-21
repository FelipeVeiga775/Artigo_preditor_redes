"""
Inspeção inicial da base UNSW-NB15.

Este script:
- carrega os arquivos de treino e teste;
- mostra dimensões e colunas;
- verifica a distribuição da variável-alvo;
- identifica valores ausentes e linhas duplicadas;
- identifica atributos categóricos;
- verifica colunas que devem ser excluídas das entradas do modelo;
- não treina modelos e não altera os arquivos originais.
"""

from pathlib import Path
import sys

import pandas as pd


# A raiz do projeto é a pasta acima de "src".
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "dados"

TRAIN_FILE = DATA_DIR / "UNSW_NB15_training-set.csv"
TEST_FILE = DATA_DIR / "UNSW_NB15_testing-set.csv"

TARGET_COLUMN = "label"

# Colunas que não devem ser usadas como atributos de entrada neste
# experimento binário. "attack_cat" revela a categoria do ataque e
# "id" é um identificador, não uma característica de tráfego.
COLUMNS_TO_EXCLUDE = {"id", "attack_cat", TARGET_COLUMN}


def load_csv(path: Path, description: str) -> pd.DataFrame:
    """Carrega um CSV e apresenta uma mensagem clara em caso de erro."""
    if not path.exists():
        raise FileNotFoundError(
            f"Não encontrei o arquivo de {description}:\n"
            f"  {path}\n\n"
            "Baixe os CSVs da página oficial da UNSW-NB15 e coloque-os "
            "na pasta 'dados'. Confira também se os nomes dos arquivos "
            "correspondem às constantes TRAIN_FILE e TEST_FILE."
        )

    print(f"\nCarregando {description}: {path.name}")
    return pd.read_csv(path, low_memory=False)


def show_basic_info(df: pd.DataFrame, name: str) -> None:
    """Exibe dimensões, colunas e tipos de dados."""
    print("\n" + "=" * 72)
    print(f"INFORMAÇÕES GERAIS — {name}")
    print("=" * 72)
    print(f"Número de linhas: {df.shape[0]:,}")
    print(f"Número de colunas: {df.shape[1]}")

    print("\nColunas e tipos:")
    for column, dtype in df.dtypes.items():
        print(f"  - {column}: {dtype}")


def show_target_distribution(df: pd.DataFrame, name: str) -> None:
    """Mostra a contagem e a proporção de cada classe do alvo."""
    print("\n" + "-" * 72)
    print(f"DISTRIBUIÇÃO DO ALVO — {name}")
    print("-" * 72)

    if TARGET_COLUMN not in df.columns:
        print(
            f"ERRO: a coluna '{TARGET_COLUMN}' não existe. "
            "Confira os nomes das colunas do arquivo."
        )
        return

    counts = df[TARGET_COLUMN].value_counts(dropna=False).sort_index()
    percentages = (
        df[TARGET_COLUMN]
        .value_counts(normalize=True, dropna=False)
        .sort_index() * 100
    )

    print("Valores encontrados:")
    for value, count in counts.items():
        print(f"  Classe {value}: {count:,} registros ({percentages[value]:.2f}%)")

    if df[TARGET_COLUMN].isna().any():
        print("ATENÇÃO: há valores ausentes na variável-alvo.")

    observed = set(df[TARGET_COLUMN].dropna().unique())
    if not observed.issubset({0, 1}):
        print(
            "ATENÇÃO: o alvo não contém apenas 0 e 1. "
            "Precisamos verificar o formato dos rótulos antes de treinar."
        )


def show_data_quality(df: pd.DataFrame, name: str) -> None:
    """Verifica valores ausentes, duplicatas e colunas constantes."""
    print("\n" + "-" * 72)
    print(f"QUALIDADE DOS DADOS — {name}")
    print("-" * 72)

    missing = df.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)

    if missing.empty:
        print("Valores ausentes: nenhum encontrado com pandas.")
    else:
        print("Colunas com valores ausentes:")
        for column, count in missing.items():
            print(f"  - {column}: {count:,}")

    duplicate_count = int(df.duplicated().sum())
    print(f"Linhas totalmente duplicadas: {duplicate_count:,}")

    constant_columns = [
        column for column in df.columns
        if df[column].nunique(dropna=False) <= 1
    ]
    if constant_columns:
        print("Colunas constantes:")
        for column in constant_columns:
            print(f"  - {column}")
    else:
        print("Colunas constantes: nenhuma encontrada.")


def show_feature_review(df: pd.DataFrame) -> None:
    """Mostra atributos categóricos e colunas excluídas do modelo."""
    print("\n" + "-" * 72)
    print("REVISÃO DOS ATRIBUTOS PARA O EXPERIMENTO")
    print("-" * 72)

    excluded_present = [
        column for column in df.columns
        if column in COLUMNS_TO_EXCLUDE
    ]
    print(
        "Colunas reservadas para exclusão das entradas do modelo: "
        + (", ".join(excluded_present) if excluded_present else "nenhuma encontrada")
    )

    features = [
        column for column in df.columns
        if column not in COLUMNS_TO_EXCLUDE
    ]
    categorical = [
        column for column in features
        if (
            pd.api.types.is_object_dtype(df[column])
            or isinstance(df[column].dtype, pd.CategoricalDtype)
        )
    ]

    print(f"Quantidade inicial de atributos candidatos: {len(features)}")
    if categorical:
        print("Atributos categóricos que provavelmente exigirão tratamento:")
        for column in categorical:
            examples = df[column].dropna().astype(str).unique()[:5]
            print(f"  - {column} (exemplos: {', '.join(examples)})")
    else:
        print("Nenhum atributo categórico textual encontrado.")

    if TARGET_COLUMN not in df.columns:
        print(
            f"ATENÇÃO: a coluna-alvo '{TARGET_COLUMN}' não foi encontrada; "
            "a lista de atributos ainda não pode ser validada."
        )


def compare_train_test_columns(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame
) -> None:
    """Verifica se treino e teste possuem as mesmas colunas."""
    print("\n" + "-" * 72)
    print("COMPARAÇÃO ENTRE TREINO E TESTE")
    print("-" * 72)

    train_columns = set(train_df.columns)
    test_columns = set(test_df.columns)

    only_train = sorted(train_columns - test_columns)
    only_test = sorted(test_columns - train_columns)

    if not only_train and not only_test:
        print("Os arquivos possuem o mesmo conjunto de colunas.")
    else:
        if only_train:
            print(f"Colunas presentes apenas no treino: {only_train}")
        if only_test:
            print(f"Colunas presentes apenas no teste: {only_test}")
        print("ATENÇÃO: precisamos investigar essa diferença antes do treinamento.")


def main() -> int:
    """Executa a inspeção inicial."""
    print("=" * 72)
    print("INSPEÇÃO INICIAL DA BASE UNSW-NB15")
    print("=" * 72)

    try:
        train_df = load_csv(TRAIN_FILE, "treinamento")
        test_df = load_csv(TEST_FILE, "teste")
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as error:
        print(f"\nNão foi possível carregar a base:\n{error}")
        return 1

    show_basic_info(train_df, "TREINAMENTO")
    show_target_distribution(train_df, "TREINAMENTO")
    show_data_quality(train_df, "TREINAMENTO")
    show_feature_review(train_df)

    show_basic_info(test_df, "TESTE")
    show_target_distribution(test_df, "TESTE")
    show_data_quality(test_df, "TESTE")
    show_feature_review(test_df)

    compare_train_test_columns(train_df, test_df)

    print("\n" + "=" * 72)
    print("INSPEÇÃO CONCLUÍDA")
    print("=" * 72)
    print(
        "Este script apenas inspeciona os dados. Nenhuma linha foi removida, "
        "nenhum arquivo foi alterado e nenhum modelo foi treinado."
    )
    print(
        "Próxima etapa: decidir e documentar o pré-processamento e a validação "
        "antes de treinar os três modelos."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
