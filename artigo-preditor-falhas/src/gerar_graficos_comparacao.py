
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Identifica a pasta principal do projeto.
PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_RESULTADOS = PASTA_PROJETO / "resultados"

arquivo_csv = PASTA_RESULTADOS / "comparacao_modelos.csv"
dados = pd.read_csv(arquivo_csv)

# Gráfico 1: comparação das métricas de classificação.
metricas = ["Acurácia", "Precisão", "Recall", "F1-score"]

dados.plot(
    x="Modelo",
    y=metricas,
    kind="bar",
    figsize=(10, 6),
    ylim=(0, 1),
    rot=0
)

plt.title("Comparação das métricas dos modelos")
plt.ylabel("Valor da métrica")
plt.xlabel("Modelo")
plt.legend(title="Métrica")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    PASTA_RESULTADOS / "comparacao_metricas.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Gráfico 2: tempo de treinamento.
plt.figure(figsize=(9, 5))
plt.bar(
    dados["Modelo"],
    dados["Tempo de treinamento (s)"]
)

plt.title("Tempo de treinamento dos modelos")
plt.ylabel("Tempo (segundos)")
plt.xlabel("Modelo")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    PASTA_RESULTADOS / "comparacao_treinamento.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Gráfico 3: tempo de previsão.
plt.figure(figsize=(9, 5))
plt.bar(
    dados["Modelo"],
    dados["Tempo de previsão (s)"]
)

plt.title("Tempo de previsão no conjunto de testes")
plt.ylabel("Tempo (segundos)")
plt.xlabel("Modelo")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    PASTA_RESULTADOS / "comparacao_previsao.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("Gráficos gerados com sucesso:")
print("- resultados/comparacao_metricas.png")
print("- resultados/comparacao_treinamento.png")
print("- resultados/comparacao_previsao.png")
