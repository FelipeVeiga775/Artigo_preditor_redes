
from pathlib import Path
import time

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.tree import plot_tree, DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from preparar_dados import preparar_dados


SEMENTE = 42
PASTA_RESULTADOS = Path(__file__).resolve().parent.parent / "resultados"
PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)


def analisar_interpretabilidade():
    print("Preparando os dados...")

    X_treino, X_teste, y_treino, y_teste, transformador = preparar_dados()

    # Recupera os nomes das 194 características após a transformação.
    nomes_caracteristicas = transformador.get_feature_names_out()

    modelos = {
        "Decision Tree": DecisionTreeClassifier(
            random_state=SEMENTE,
            class_weight="balanced"
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=SEMENTE,
            class_weight="balanced",
            n_jobs=-1
        ),
        "XGBoost": XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=SEMENTE,
            eval_metric="logloss",
            n_jobs=-1
        )
    }

    importancias = {}

    for nome, modelo in modelos.items():
        print(f"\nTreinando {nome} para análise...")

        inicio = time.perf_counter()
        modelo.fit(X_treino, y_treino)
        duracao = time.perf_counter() - inicio

        print(f"Treinamento concluído em {duracao:.2f} segundos.")

        # A árvore será exibida somente até o terceiro nível,
        # para manter o desenho legível.
        if nome == "Decision Tree":
            plt.figure(figsize=(24, 12))

            plot_tree(
                modelo,
                max_depth=3,
                feature_names=nomes_caracteristicas,
                class_names=["Normal (0)", "Ataque (1)"],
                filled=True,
                rounded=True,
                fontsize=8
            )

            plt.title("Decision Tree - Primeiros níveis")
            plt.tight_layout()

            plt.savefig(
                PASTA_RESULTADOS / "arvore_decision_tree.png",
                dpi=200,
                bbox_inches="tight"
            )
            plt.close()

        # Random Forest e XGBoost fornecem importâncias
        # para as características utilizadas no treinamento.
        if nome in ["Random Forest", "XGBoost"]:
            importancias[nome] = modelo.feature_importances_

    # Monta uma tabela com as importâncias dos dois modelos.
    tabela = pd.DataFrame({
        "caracteristica": nomes_caracteristicas,
        "random_forest": importancias["Random Forest"],
        "xgboost": importancias["XGBoost"]
    })

    tabela.to_csv(
        PASTA_RESULTADOS / "importancia_caracteristicas.csv",
        index=False,
        encoding="utf-8-sig"
    )

    # Gera um gráfico para cada modelo, com as 15 características
    # de maior importância.
    for nome, coluna in [
        ("Random Forest", "random_forest"),
        ("XGBoost", "xgboost")
    ]:
        top_15 = tabela.nlargest(15, coluna).sort_values(coluna)

        plt.figure(figsize=(12, 8))
        plt.barh(top_15["caracteristica"], top_15[coluna])

        plt.xlabel("Importância")
        plt.ylabel("Característica")
        plt.title(f"15 características mais importantes - {nome}")
        plt.tight_layout()

        nome_arquivo = nome.lower().replace(" ", "_")
        plt.savefig(
            PASTA_RESULTADOS / f"importancia_{nome_arquivo}.png",
            dpi=200,
            bbox_inches="tight"
        )
        plt.close()

    print("\nAnálise de interpretabilidade concluída!")
    print(f"Arquivos salvos em: {PASTA_RESULTADOS}")


if __name__ == "__main__":
    analisar_interpretabilidade()
