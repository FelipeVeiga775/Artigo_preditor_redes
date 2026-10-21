# Preditor de Falhas em Redes — Detecção de Intrusões

Projeto acadêmico de aprendizado de máquina aplicado à segurança de redes, com foco na detecção de tráfego malicioso utilizando o conjunto de dados **UNSW-NB15**.

O trabalho compara três algoritmos de classificação — Decision Tree, Random Forest e XGBoost — considerando métricas de desempenho preditivo e tempo de execução.

## Acesso ao projeto

- **Site publicado:** [Artigo do Preditor de Falhas](https://felipeveiga775.github.io/Artigo_preditor_redes/)
- **Repositório:** [Artigo_preditor_redes no GitHub](https://github.com/FelipeVeiga775/Artigo_preditor_redes)

## Objetivos

- Investigar o uso de aprendizado de máquina na detecção de intrusões em redes.
- Comparar diferentes algoritmos de classificação aplicados ao mesmo problema.
- Avaliar o desempenho dos modelos por meio de métricas de classificação.
- Analisar os tempos de treinamento e previsão.
- Documentar os procedimentos experimentais e apresentar os resultados em um artigo acadêmico.

## Conjunto de dados

O projeto utiliza o **UNSW-NB15**, conjunto de dados criado para pesquisas em segurança de redes, contendo registros de tráfego normal e de diferentes tipos de atividades maliciosas.

Os dados são utilizados no treinamento e na avaliação dos modelos de classificação.

**Fonte do conjunto de dados:** [UNSW Canberra Cyber — UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset).

## Algoritmos avaliados

### Decision Tree

Árvore de decisão que realiza classificações por meio de regras organizadas em nós e ramificações. É um modelo que permite interpretar parte do processo de decisão.

### Random Forest

Algoritmo que combina múltiplas árvores de decisão para produzir uma classificação, buscando melhorar a capacidade preditiva e reduzir a dependência de uma única árvore.

### XGBoost

Algoritmo de boosting que constrói modelos sequencialmente, procurando melhorar o desempenho da classificação a partir dos erros dos modelos anteriores.

## Resultados experimentais

Os resultados obtidos durante o experimento são apresentados a seguir.

| Métrica | Decision Tree | Random Forest | XGBoost |
|---|---:|---:|---:|
| Acurácia | 86,17% | 89,29% | 87,34% |
| Precisão | 81,68% | 85,19% | 81,98% |
| Recall | 96,53% | 97,51% | 98,70% |
| F1-score | 88,49% | 90,93% | 89,57% |
| Tempo de treinamento | 11,883 s | 14,979 s | 0,539 s |
| Tempo de previsão | 0,0141 s | 0,0957 s | 0,0183 s |

### Interpretação dos resultados

- **Random Forest** obteve a maior acurácia, precisão e F1-score entre os modelos avaliados.
- **XGBoost** apresentou o maior recall e o menor tempo de treinamento.
- **Decision Tree** apresentou o menor tempo de previsão no experimento.

Os resultados demonstram que o melhor modelo depende do critério considerado. O Random Forest apresentou o melhor equilíbrio segundo o F1-score, enquanto o XGBoost se destacou na identificação dos exemplos positivos e na velocidade de treinamento.

Em um cenário de detecção de intrusões, o recall é especialmente relevante, pois indica a proporção dos exemplos positivos reais identificados pelo modelo. Entretanto, a precisão também deve ser considerada para compreender a ocorrência de falsos positivos.

Os tempos medidos correspondem ao ambiente experimental utilizado e não constituem garantias de desempenho em outros equipamentos ou cenários.

## Métricas utilizadas

- **Acurácia:** proporção de previsões corretas em relação ao total de exemplos avaliados.
- **Precisão:** proporção de previsões positivas que correspondem a exemplos realmente positivos.
- **Recall:** proporção dos exemplos positivos reais identificados corretamente.
- **F1-score:** média harmônica entre precisão e recall.
- **Tempo de treinamento:** tempo necessário para ajustar o modelo aos dados de treinamento.
- **Tempo de previsão:** tempo medido para gerar as previsões durante a avaliação.

A interpretação dessas métricas deve considerar o contexto do problema, a distribuição das classes e os custos associados a falsos positivos e falsos negativos.

## Tecnologias e ferramentas

- **Python:** desenvolvimento dos experimentos de aprendizado de máquina.
- **UNSW-NB15:** conjunto de dados para avaliação dos modelos.
- **HTML, CSS e JavaScript:** desenvolvimento da interface web.
- **Git e GitHub:** versionamento e hospedagem do projeto.
- **GitHub Pages:** publicação do site.
- **GitHub Actions:** automação do processo de publicação.

## Site do projeto

O site apresenta o projeto e serve como ponto de acesso à documentação e aos resultados disponibilizados.

A publicação é realizada pelo GitHub Actions. O workflow de implantação está localizado em `.github/workflows/deploy.yml` e publica o conteúdo do diretório configurado no arquivo.

**Acesse:** [https://felipeveiga775.github.io/Artigo_preditor_redes/](https://felipeveiga775.github.io/Artigo_preditor_redes/)

## Reprodutibilidade

A reprodução dos experimentos depende dos arquivos de código, dos dados utilizados, das bibliotecas necessárias e das configurações do ambiente.

Para tornar a execução reproduzível por terceiros, o repositório deve disponibilizar ou documentar:

1. Os scripts utilizados no processamento dos dados, treinamento e avaliação.
2. As dependências e suas versões relevantes.
3. A origem e as instruções de obtenção dos dados.
4. Os comandos necessários para executar os experimentos.
5. Os procedimentos utilizados para calcular e registrar as métricas.

As instruções de execução devem corresponder aos arquivos efetivamente presentes no repositório.

## Limitações

Os resultados representam o desempenho observado no experimento realizado com o conjunto de dados utilizado. Eles não garantem desempenho equivalente em redes reais ou em conjuntos de dados diferentes.

Uma aplicação prática exigiria avaliações adicionais, incluindo testes em outros cenários, análise de falsos positivos e falsos negativos, investigação de possíveis vieses dos dados e monitoramento do desempenho ao longo do tempo.

Os resultados também devem ser interpretados considerando as condições experimentais e o ambiente computacional em que as medições foram realizadas.

## Contexto acadêmico

Este projeto foi desenvolvido no contexto de uma atividade acadêmica, com o objetivo de estudar e comparar algoritmos de aprendizado de máquina aplicados à detecção de intrusões em redes de computadores.

O trabalho reúne experimentação, análise comparativa de métricas, documentação técnica e apresentação dos resultados por meio de um site publicado.

## Como executar o projeto

### 1. Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- [Python](https://www.python.org/downloads/) 3.10 ou superior;
- [Git](https://git-scm.com/downloads);
- `pip`, gerenciador de pacotes do Python.

### 2. Clonar o repositório

Abra o terminal e execute os seguintes comandos:

```bash
git clone https://github.com/FelipeVeiga775/Artigo_preditor_redes.git
cd Artigo_preditor_redes/artigo-preditor-falhas
```

### 3. Criar um ambiente virtual

Recomenda-se utilizar um ambiente virtual para isolar as dependências do projeto.

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux ou macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

No Windows, caso o comando `python` não seja reconhecido, utilize `py -m pip` no lugar de `python -m pip`.

### 5. Verificar os dados

Confira se os arquivos do conjunto de dados UNSW-NB15 estão presentes na pasta `dados/`:

```text
dados/
├── UNSW_NB15_training-set.csv
└── UNSW_NB15_testing-set.csv
```

Esses arquivos são utilizados para treinar e avaliar os modelos de classificação.

### 6. Preparar os dados

Execute o script de preparação:

```bash
python src/preparar_dados.py
```

Essa etapa prepara as características utilizadas pelos modelos, separa os rótulos de classificação e realiza a codificação das variáveis categóricas.

### 7. Treinar e avaliar os modelos

Execute o script principal:

```bash
python src/treinar_modelos.py
```

O script treina e avalia os três algoritmos utilizados no projeto:

- **Decision Tree**
- **Random Forest**
- **XGBoost**

Os resultados incluem métricas de classificação, tempos de execução e matrizes de confusão, salvos na pasta `resultados/`.

### 8. Analisar a interpretabilidade

Para gerar a visualização da árvore de decisão e analisar a importância das características dos modelos, execute:

```bash
python src/analisar_interpretabilidade.py
```

Os arquivos gerados permitem visualizar a estrutura da árvore e identificar as características mais relevantes para as previsões.

### 9. Gerar os gráficos comparativos

Após gerar os resultados do treinamento, execute:

```bash
python src/gerar_graficos_comparacao.py
```

Esse script gera gráficos para comparar:

- As métricas de classificação dos modelos;
- O tempo de treinamento;
- O tempo de previsão.

### Observações

- Execute os comandos a partir da pasta `artigo-preditor-falhas/`.
- No Windows, os comandos que utilizam `python` também podem ser executados com `py`, caso necessário.
- Os tempos de treinamento e previsão podem variar conforme o hardware e as condições de execução.
- Os scripts de análise dependem dos arquivos de resultados gerados pelas etapas anteriores.
- Os arquivos CSV do conjunto UNSW-NB15 devem estar nos caminhos esperados pelo projeto.


