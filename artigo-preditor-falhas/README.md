# Artigo do Preditor de Falhas — inspeção inicial

Projeto acadêmico independente para comparar Árvore de Decisão, Random Forest e XGBoost na detecção binária de intrusão em redes.

## Estrutura

```text
artigo-preditor-falhas/
├── dados/
│   ├── UNSW_NB15_training-set.csv
│   └── UNSW_NB15_testing-set.csv
├── src/
│   └── inspecionar_dados.py
├── requirements.txt
└── README.md
```

## 1. Obter os dados

Baixe os arquivos de treinamento e teste da página oficial da UNSW-NB15:

https://research.unsw.edu.au/projects/unsw-nb15-dataset

Coloque os CSVs na pasta `dados/`. O script espera os nomes `UNSW_NB15_training-set.csv` e `UNSW_NB15_testing-set.csv`. Se os arquivos tiverem outros nomes, altere `TRAIN_FILE` e `TEST_FILE` em `src/inspecionar_dados.py`.

Não publique arquivos de dados grandes no repositório sem antes conferir os termos de uso e as orientações da disciplina.

## 2. Instalar dependências

Recomenda-se Python 3.11 ou 3.12 em um ambiente virtual.

Windows:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Executar a inspeção

Na raiz do projeto:

```bash
python src/inspecionar_dados.py
```

O programa mostra dimensões, colunas, tipos, distribuição do alvo, valores ausentes, duplicatas, atributos categóricos e diferenças entre os arquivos de treino e teste.

## Escopo atual

Este script **não treina modelos**, não altera os CSVs e não toma decisões automáticas de limpeza. Os resultados da inspeção devem ser avaliados antes de definir o pré-processamento e o protocolo experimental.

Para a tarefa binária, o alvo esperado é `label` (0 = normal; 1 = ataque). As colunas `id` e `attack_cat` são marcadas para exclusão das entradas do modelo: a primeira é identificadora e a segunda revela a categoria do ataque. Essa decisão deve ser registrada no artigo.
