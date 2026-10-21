
from pathlib import Path
from time import perf_counter

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.base import clone
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
)
from xgboost import XGBClassifier

from preparar_dados import preparar_dados


# Diretório para salvar os resultados
PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_DIR / "resultados"
RESULTS_DIR.mkdir(exist_ok=True)

SEMENTE = 42


def criar_modelos():
    """Cria os três modelos com configurações iniciais documentadas."""

    return {
        "Decision Tree": DecisionTreeClassifier(
            random_state=SEMENTE,
            class_weight="balanced",
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=SEMENTE,
            class_weight="balanced",
            n_jobs=-1,
        ),
        "XGBoost": XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=SEMENTE,
            eval_metric="logloss",
            n_jobs=-1,
        ),
    }


def avaliar_modelo(nome, modelo, X_treino, X_teste, y_treino, y_teste):
    """Treina, mede o tempo e avalia um modelo."""

    print(f"\nTreinando {nome}...")
    
    inicio_treino = perf_counter()
    modelo.fit(X_treino, y_treino)
    tempo_treino = perf_counter() - inicio_treino

    inicio_previsao = perf_counter()
    previsoes = modelo.predict(X_teste)
    tempo_previsao = perf_counter() - inicio_previsao

    # A classe 1 representa tráfego malicioso.
    metricas = {
        "Modelo": nome,
        "Acurácia": accuracy_score(y_teste, previsoes),
        "Precisão": precision_score(
            y_teste, previsoes, pos_label=1, zero_division=0
        ),
        "Recall": recall_score(
            y_teste, previsoes, pos_label=1, zero_division=0
        ),
        "F1-score": f1_score(
            y_teste, previsoes, pos_label=1, zero_division=0
        ),
        "Tempo de treinamento (s)": tempo_treino,
        "Tempo de previsão (s)": tempo_previsao,
    }

    matriz = confusion_matrix(y_teste, previsoes, labels=[0, 1])

    print(f"Tempo de treinamento: {tempo_treino:.2f} segundos")
    print(f"Tempo de previsão: {tempo_previsao:.2f} segundos")
    print(f"Precisão: {metricas['Precisão']:.4f}")
    print(f"Recall: {metricas['Recall']:.4f}")
    print(f"F1-score: {metricas['F1-score']:.4f}")

    # Salva a matriz de confusão de cada modelo.
    exibicao = ConfusionMatrixDisplay(
        confusion_matrix=matriz,
        display_labels=["Normal (0)", "Ataque (1)"],
    )
    exibicao.plot(values_format="d", cmap="Blues")
    plt.title(f"Matriz de confusão — {nome}")
    plt.tight_layout()

    nome_arquivo = nome.lower().replace(" ", "_")
    plt.savefig(RESULTS_DIR / f"matriz_{nome_arquivo}.png", dpi=150)
    plt.close()

    return metricas, matriz


def main():
    print("=" * 65)
    print("EXPERIMENTO — DETECÇÃO DE INTRUSÕES UNSW-NB15")
    print("=" * 65)

    X_treino, X_teste, y_treino, y_teste, _ = preparar_dados()

    modelos = criar_modelos()
    resultados = []
    matrizes = {}

    for nome, modelo in modelos.items():
        metricas, matriz = avaliar_modelo(
            nome,
            modelo,
            X_treino,
            X_teste,
            y_treino,
            y_teste,
        )
        resultados.append(metricas)
        matrizes[nome] = matriz

    tabela = pd.DataFrame(resultados)
    caminho_csv = RESULTS_DIR / "comparacao_modelos.csv"
    tabela.to_csv(caminho_csv, index=False, encoding="utf-8-sig")

    print("\n" + "=" * 65)
    print("COMPARAÇÃO FINAL")
    print("=" * 65)
    print(tabela.round(4).to_string(index=False))

    print(f"\nResultados salvos em: {RESULTS_DIR}")
    print("Arquivos gerados:")
    print("- comparacao_modelos.csv")
    print("- matrizes de confusão dos três modelos")


if __name__ == "__main__":
    main()
