
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# Caminhos dos arquivos
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "dados"

TRAIN_FILE = DATA_DIR / "UNSW_NB15_training-set.csv"
TEST_FILE = DATA_DIR / "UNSW_NB15_testing-set.csv"

TARGET = "label"
COLUNAS_EXCLUIDAS = ["id", "attack_cat"]


def carregar_dados():
    """Carrega os arquivos de treinamento e teste."""

    if not TRAIN_FILE.exists():
        raise FileNotFoundError(
            f"Arquivo de treinamento não encontrado: {TRAIN_FILE}"
        )

    if not TEST_FILE.exists():
        raise FileNotFoundError(
            f"Arquivo de teste não encontrado: {TEST_FILE}"
        )

    treino = pd.read_csv(TRAIN_FILE)
    teste = pd.read_csv(TEST_FILE)

    return treino, teste


def preparar_dados():
    """Separa atributos e alvo e prepara o codificador."""

    treino, teste = carregar_dados()

    # Confere se os arquivos possuem as colunas esperadas
    if TARGET not in treino.columns or TARGET not in teste.columns:
        raise ValueError("A coluna 'label' não existe nos dois arquivos.")

    if not treino.columns.equals(teste.columns):
        raise ValueError(
            "Os arquivos de treinamento e teste possuem "
            "colunas diferentes ou em ordem diferente."
        )

    if treino[TARGET].isna().any() or teste[TARGET].isna().any():
        raise ValueError("A coluna 'label' possui valores ausentes.")

    # Separa aquilo que o modelo aprenderá daquilo que deve prever
    X_treino = treino.drop(
        columns=[TARGET] + COLUNAS_EXCLUIDAS
    )
    X_teste = teste.drop(
        columns=[TARGET] + COLUNAS_EXCLUIDAS
    )

    y_treino = treino[TARGET]
    y_teste = teste[TARGET]

    # Identifica automaticamente colunas categóricas e numéricas
    colunas_categoricas = X_treino.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    colunas_numericas = X_treino.select_dtypes(
        include=["number", "bool"]
    ).columns.tolist()

    # Transforma categorias em colunas numéricas.
    # Categorias desconhecidas no teste serão ignoradas.
    transformador = ColumnTransformer(
        transformers=[
            (
                "categoricas",
                OneHotEncoder(handle_unknown="ignore"),
                colunas_categoricas,
            ),
            (
                "numericas",
                "passthrough",
                colunas_numericas,
            ),
        ],
        remainder="drop",
    )

    # IMPORTANTE: aprende a transformação somente no treinamento.
    X_treino_preparado = transformador.fit_transform(X_treino)

    # Aplica a mesma transformação ao teste, sem reaprender.
    X_teste_preparado = transformador.transform(X_teste)

    return (
        X_treino_preparado,
        X_teste_preparado,
        y_treino,
        y_teste,
        transformador,
    )


def main():
    print("=" * 65)
    print("PREPARAÇÃO DOS DADOS — UNSW-NB15")
    print("=" * 65)

    try:
        (
            X_treino,
            X_teste,
            y_treino,
            y_teste,
            transformador,
        ) = preparar_dados()

        print("\nPreparação concluída!")
        print(f"Registros de treinamento: {X_treino.shape[0]:,}")
        print(f"Registros de teste: {X_teste.shape[0]:,}")
        print(f"Atributos após a transformação: {X_treino.shape[1]:,}")

        print("\nDistribuição do alvo no treinamento:")
        print(y_treino.value_counts().sort_index())

        print("\nDistribuição do alvo no teste:")
        print(y_teste.value_counts().sort_index())

        print("\nFormato dos dados:")
        print(f"Treinamento: {X_treino.shape}")
        print(f"Teste: {X_teste.shape}")

        print("\nVerificação:")
        print("O transformador foi ajustado somente no treinamento.")
        print("Os dados de teste não foram usados para aprender a transformação.")
        print("Nenhum modelo foi treinado.")
        print("Nenhum arquivo CSV foi alterado.")

    except (FileNotFoundError, ValueError, KeyError) as erro:
        print(f"\nNão foi possível preparar os dados: {erro}")


if __name__ == "__main__":
    main()
