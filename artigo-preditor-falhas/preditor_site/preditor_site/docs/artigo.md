# Detecção de intrusões em redes: uma análise comparativa entre Decision Tree, Random Forest e XGBoost

**Autores:** Eduardo Quintino Filho, Felipe Veiga da Silva, Henrique de Aguiar Fernandes, Niccolas Lupetti dos Santos, Tharik Lima dos Santos

**Instituição:** Centro Universitário Braz Cubas

**Disciplina:** Estrutura de Dados II

**Orientadora:** Profa. Dra. Andréa Ono Sakai

**Data:** 21/10/2026

## Resumo

A detecção de intrusões em redes é uma atividade importante para a segurança da informação, pois permite identificar padrões de tráfego associados a possíveis atividades maliciosas. Nesse contexto, algoritmos de aprendizado de máquina podem auxiliar na classificação de registros de rede como normais ou suspeitos. Este trabalho apresenta uma análise comparativa entre os algoritmos Decision Tree, Random Forest e XGBoost aplicados à detecção de intrusões, utilizando o conjunto de dados público UNSW-NB15. Os modelos foram treinados com o conjunto oficial de treinamento e avaliados no conjunto oficial de teste, considerando acurácia, precisão, recall, F1-score, tempo de treinamento, tempo de previsão e matrizes de confusão. Os resultados obtidos indicaram que o Random Forest apresentou o maior F1-score, de 90,93%, enquanto o XGBoost alcançou o maior recall, de 98,70%, identificando a maior proporção de ataques presentes no conjunto de teste. O XGBoost também apresentou o menor tempo de treinamento observado. A análise evidencia que a escolha do algoritmo depende das prioridades da aplicação, especialmente do equilíbrio entre desempenho, custo computacional e redução de ataques não identificados.

**Palavras-chave:** aprendizado de máquina; segurança de redes; detecção de intrusões; Decision Tree; Random Forest; XGBoost.

## 1. Introdução

A crescente utilização de redes de computadores em serviços digitais, sistemas corporativos e aplicações conectadas amplia a importância da segurança das informações transmitidas. Nesse cenário, atividades maliciosas podem comprometer a disponibilidade, a integridade e a confidencialidade dos sistemas. Por isso, mecanismos capazes de identificar comportamentos suspeitos no tráfego de rede são relevantes para a prevenção e a investigação de incidentes de segurança.

Os sistemas de detecção de intrusões, conhecidos pela sigla IDS (*Intrusion Detection Systems*), buscam identificar atividades potencialmente maliciosas a partir de informações coletadas ou derivadas do tráfego de rede. Entretanto, reconhecer padrões de ataques é uma tarefa desafiadora, pois os registros podem apresentar características variadas e comportamentos diferentes entre comunicações legítimas e maliciosas.

O aprendizado de máquina oferece métodos capazes de aprender padrões a partir de conjuntos de dados previamente classificados. Entre esses métodos, os algoritmos baseados em árvores de decisão destacam-se por sua capacidade de trabalhar com dados estruturados e realizar tarefas de classificação. A Decision Tree constrói regras de decisão; o Random Forest combina várias árvores; e o XGBoost utiliza um processo de aprendizado sequencial de árvores para aprimorar as previsões.

Apesar de compartilharem uma estrutura baseada em árvores, esses algoritmos possuem diferenças importantes em seu funcionamento, desempenho computacional e interpretabilidade. Essas diferenças justificam uma avaliação comparativa utilizando o mesmo cenário de classificação.

Diante disso, este trabalho investiga a seguinte questão de pesquisa:

**Como Decision Tree, Random Forest e XGBoost se comparam na identificação de tráfego de rede malicioso, considerando desempenho de classificação, tempo de execução e interpretabilidade?**

O objetivo geral é comparar os três algoritmos na tarefa de detecção de intrusões utilizando o conjunto de dados UNSW-NB15. Como objetivos específicos, busca-se avaliar suas métricas de classificação, analisar falsos positivos e falsos negativos, comparar os tempos observados de treinamento e previsão e examinar as características que receberam maior importância nos modelos.

## 2. Fundamentação teórica

### 2.1. Detecção de intrusões e aprendizado de máquina

A detecção de intrusões consiste na identificação de atividades que podem representar violações de segurança ou comportamentos anormais em sistemas computacionais. Em uma abordagem baseada em aprendizado supervisionado, um modelo recebe exemplos rotulados durante o treinamento e aprende a relacionar suas características às classes correspondentes.

Neste trabalho, a classificação é binária: registros com rótulo 0 representam tráfego normal, enquanto registros com rótulo 1 representam tráfego malicioso. O modelo recebe características do tráfego, como quantidade de bytes transmitidos, duração da comunicação, características de conexão e informações relacionadas aos protocolos, e produz uma previsão para cada registro.

É importante observar que a classificação não comprova, isoladamente, a existência de um ataque real em uma rede em produção. Ela representa uma previsão baseada nos padrões aprendidos a partir dos dados disponíveis.

### 2.2. Decision Tree

A Decision Tree, ou árvore de decisão, é um algoritmo que organiza decisões em uma estrutura semelhante a uma árvore. Cada nó interno representa uma condição aplicada a uma característica, cada ramificação corresponde ao resultado dessa condição e cada folha representa uma classe prevista.

Por exemplo, em um sistema de detecção de intrusões, uma árvore pode avaliar o valor de uma característica de rede e, dependendo do resultado, seguir diferentes caminhos até classificar o registro como normal ou malicioso.

O treinamento procura dividir os dados de modo que os grupos resultantes apresentem maior homogeneidade em relação às classes. Entre os critérios utilizados para avaliar essas divisões está a impureza de Gini.

Uma das principais vantagens da Decision Tree é a facilidade de interpretação: suas regras podem ser visualizadas e examinadas individualmente. Por outro lado, uma árvore muito profunda pode se ajustar excessivamente aos dados de treinamento, fenômeno conhecido como *overfitting*, reduzindo sua capacidade de generalização.

### 2.3. Random Forest

O Random Forest é um algoritmo de aprendizado em conjunto, ou *ensemble learning*, proposto por Breiman (2001). Em vez de depender de uma única árvore, ele combina as previsões de diversas árvores treinadas com mecanismos de aleatoriedade.

De maneira simplificada, cada árvore produz uma classificação, e o modelo combina as respostas para determinar a classe final. A diversidade entre as árvores ajuda a reduzir a dependência de uma única estrutura de decisão e pode melhorar a capacidade de generalização.

Uma vantagem do Random Forest é que ele costuma apresentar bom desempenho em conjuntos de dados estruturados e permite estimar a importância das características utilizadas pelas árvores. Entretanto, a combinação de muitas árvores aumenta o custo computacional e torna a interpretação do conjunto completo mais difícil do que a análise de uma única árvore.

### 2.4. XGBoost

O XGBoost, apresentado por Chen e Guestrin (2016), é uma implementação otimizada de *gradient boosting* baseada em árvores de decisão. Nesse método, as árvores são construídas sequencialmente, de forma que as etapas posteriores contribuam para reduzir os erros do modelo acumulado.

Diferentemente do Random Forest, que combina árvores construídas de maneira relativamente independente, o XGBoost utiliza uma estratégia de aprimoramento progressivo. O algoritmo também incorpora mecanismos de regularização e otimizações computacionais para melhorar o desempenho e controlar a complexidade do modelo.

O XGBoost pode alcançar resultados competitivos em tarefas de classificação e oferece recursos para examinar a importância das características. Entretanto, sua interpretação exige mais cuidado do que a leitura direta de uma árvore simples, e seu desempenho depende das configurações utilizadas durante o treinamento.

### 2.5. Exemplo ilustrativo de classificação

Considere um registro de comunicação de rede que apresente duração, quantidade de bytes enviados e recebidos, protocolo e estado da conexão.

Uma Decision Tree poderia aplicar uma sequência de condições sobre essas características até chegar a uma classificação. O Random Forest avaliaria o registro por meio de várias árvores e combinaria suas previsões. O XGBoost, por sua vez, utilizaria um conjunto de árvores construído progressivamente durante o treinamento.

Os três modelos recebem os mesmos dados de entrada no experimento, mas podem aprender padrões diferentes e, consequentemente, produzir resultados distintos.

**Figura 1 — Primeiros níveis da árvore de decisão treinada.**

![Árvore de decisões](../resultados/arvore_decision_tree.png)

A figura gerada no experimento mostra que a primeira divisão da árvore utiliza a característica `sttl`, com o limiar 61. Isso demonstra como o modelo cria regras a partir das características disponíveis. Esse exemplo descreve uma divisão aprendida pelo modelo, não uma regra universal que determine se qualquer comunicação é maliciosa.

## 3. Metodologia

### 3.1. Tipo de pesquisa e ambiente experimental

O trabalho caracteriza-se como um experimento quantitativo e comparativo, no qual três algoritmos de classificação são avaliados sobre o mesmo problema. A implementação foi realizada em Python, utilizando pandas para manipulação dos dados, scikit-learn para pré-processamento e implementação de modelos, XGBoost para o terceiro algoritmo e bibliotecas de visualização para a geração dos gráficos.

A semente aleatória foi fixada em 42 para favorecer a reprodutibilidade. As versões exatas das bibliotecas e as especificações do equipamento devem ser registradas na versão final do artigo, pois podem influenciar os tempos de execução.

### 3.2. Conjunto de dados

Foi utilizado o conjunto de dados UNSW-NB15, disponibilizado para pesquisas em detecção de intrusões pela University of New South Wales. O conjunto contém registros de tráfego normal e atividades de ataque, representados por características numéricas e categóricas.

Foram utilizados os arquivos oficiais:

- `UNSW_NB15_training-set.csv`: 175.341 registros.
- `UNSW_NB15_testing-set.csv`: 82.332 registros.

Os dois arquivos contêm originalmente 45 colunas. A variável-alvo escolhida foi `label`, que identifica o tráfego normal com o valor 0 e o tráfego de ataque com o valor 1.

A coluna `id` foi removida por representar a identificação do registro, e `attack_cat` foi excluída por descrever a categoria do ataque. A exclusão de `attack_cat` evita que o modelo utilize uma informação diretamente associada à natureza da atividade maliciosa para prever a classificação binária.

### 3.3. Preparação dos dados

Os dados foram carregados e inspecionados antes do treinamento. Na inspeção inicial, não foram identificados valores ausentes pelo procedimento de verificação utilizado, registros integralmente duplicados ou colunas constantes.

As características categóricas `proto`, `service` e `state` foram transformadas por codificação one-hot. Esse procedimento cria variáveis binárias para representar as categorias. As características numéricas foram mantidas em seus valores originais.

O pré-processador foi ajustado apenas sobre o conjunto de treinamento. Depois, a transformação aprendida foi aplicada ao conjunto de teste, sem reajustar o codificador com os dados de teste. Essa separação reduz o risco de vazamento de informações entre treinamento e avaliação.

Após a transformação, o conjunto de treinamento passou a conter 194 características, e o conjunto de teste também passou a conter 194 características.

A distribuição da variável-alvo não é idêntica nos dois arquivos. No treinamento, 68,06% dos registros pertencem à classe de ataques e 31,94% à classe normal. No teste, 55,06% correspondem a ataques e 44,94% a tráfego normal. Essa diferença deve ser considerada na interpretação das métricas.

### 3.4. Configuração dos modelos

Foram utilizadas as seguintes configurações:

| Algoritmo | Configuração principal |
|---|---|
| Decision Tree | `random_state=42`; `class_weight="balanced"` |
| Random Forest | 100 árvores; `random_state=42`; `class_weight="balanced"`; `n_jobs=-1` |
| XGBoost | 100 estimadores; profundidade máxima 6; taxa de aprendizado 0,1; `random_state=42`; `eval_metric="logloss"`; `n_jobs=-1` |

Os parâmetros não especificados permaneceram com os valores padrão das respectivas implementações. O parâmetro `class_weight="balanced"` foi utilizado na Decision Tree e no Random Forest, mas não foi configurada ponderação explícita equivalente no XGBoost.

Portanto, a comparação utiliza o mesmo conjunto de dados e o mesmo pré-processamento, mas não configurações inteiramente equivalentes de tratamento das classes. Além disso, não foi realizada uma busca exaustiva de hiperparâmetros. Essas condições são consideradas limitações metodológicas.

### 3.5. Métricas de avaliação

Os modelos foram avaliados no conjunto de teste, considerando as seguintes métricas:

**Acurácia:** mede a proporção de previsões corretas entre todos os registros.

\[
\text{Acurácia}=\frac{VP+VN}{VP+VN+FP+FN}
\]

**Precisão:** mede a proporção de previsões de ataque que realmente correspondem a ataques.

\[
\text{Precisão}=\frac{VP}{VP+FP}
\]

**Recall:** mede a proporção de ataques reais identificados corretamente.

\[
\text{Recall}=\frac{VP}{VP+FN}
\]

**F1-score:** representa a média harmônica entre precisão e recall.

\[
F1=2\cdot\frac{\text{Precisão}\cdot\text{Recall}}{\text{Precisão}+\text{Recall}}
\]

Nas fórmulas, VP representa verdadeiros positivos, VN verdadeiros negativos, FP falsos positivos e FN falsos negativos. A classe positiva é a classe de ataques (`label = 1`).

Também foram registradas as matrizes de confusão e os tempos de treinamento e previsão. O tempo de previsão corresponde ao processamento de todo o conjunto de teste, composto por 82.332 registros, e não ao tempo de uma única previsão.

### 3.6. Análise de interpretabilidade

A interpretabilidade foi examinada por meio da visualização dos primeiros níveis da Decision Tree e das importâncias de características disponibilizadas pelo Random Forest e pelo XGBoost.

Essas importâncias indicam quais características contribuíram mais para as divisões ou para o funcionamento dos modelos, conforme o critério interno de cada algoritmo. Elas não demonstram, por si só, que uma característica causa ataques ou que seja suficiente para identificá-los em qualquer rede.

## 4. Resultados e discussão

### 4.1. Comparação das métricas de classificação

Os resultados observados no conjunto de teste estão apresentados na Tabela 1.

**Tabela 1 — Métricas de classificação dos modelos.**

| Modelo | Acurácia | Precisão | Recall | F1-score |
|---|---:|---:|---:|---:|
| Decision Tree | 86,17% | 81,68% | 96,53% | 88,49% |
| Random Forest | 89,29% | 85,19% | 97,51% | 90,93% |
| XGBoost | 87,34% | 81,98% | 98,70% | 89,57% |

[Inserir o gráfico `comparacao_metricas.png`, utilizando o nome real do arquivo caso seja diferente.]

O Random Forest apresentou os maiores valores de acurácia, precisão e F1-score. Sua acurácia foi de 89,29%, indicando que aproximadamente nove em cada dez registros do conjunto de teste foram classificados corretamente. Além disso, o F1-score de 90,93% indica o melhor equilíbrio entre precisão e recall entre os modelos avaliados.

O XGBoost apresentou o maior recall, de 98,70%. Esse resultado indica que o algoritmo identificou uma proporção maior dos ataques presentes no conjunto de teste. Entretanto, sua precisão foi inferior à do Random Forest, demonstrando que a maior capacidade de detecção veio acompanhada de mais classificações incorretas de registros normais como ataques.

A Decision Tree apresentou o menor F1-score e a menor acurácia entre os três modelos. Apesar disso, seu recall de 96,53% mostra que ela também identificou grande parte dos ataques existentes no conjunto de teste.

Esses resultados demonstram que a escolha do algoritmo depende do objetivo operacional. Um sistema que priorize a redução de ataques não detectados pode valorizar o recall, enquanto uma aplicação que também precise limitar alarmes incorretos pode priorizar um equilíbrio entre precisão e recall.

### 4.2. Análise das matrizes de confusão

As matrizes de confusão permitem examinar os tipos de erro cometidos por cada modelo.

**Tabela 2 — Resultados das classificações no conjunto de teste.**

| Modelo | Verdadeiros negativos | Falsos positivos | Falsos negativos | Verdadeiros positivos |
|---|---:|---:|---:|---:|
| Decision Tree | 27.187 | 9.813 | 1.573 | 43.759 |
| Random Forest | 29.313 | 7.687 | 1.128 | 44.204 |
| XGBoost | 27.164 | 9.836 | 589 | 44.743 |

[Inserir as figuras `matriz_decision_tree.png`, `matriz_random_forest.png` e `matriz_xgboost.png`.]

O Random Forest apresentou 7.687 falsos positivos e 1.128 falsos negativos. Entre os três modelos, registrou a menor quantidade de falsos positivos e manteve um número elevado de ataques corretamente identificados.

O XGBoost apresentou 589 falsos negativos, o menor valor observado. Em comparação ao Random Forest, deixou de identificar 539 ataques a menos. Entretanto, produziu 2.149 falsos positivos a mais. Em uma aplicação prática, isso pode representar maior quantidade de alertas que exigem investigação.

A Decision Tree apresentou 1.573 falsos negativos e 9.813 falsos positivos. Embora tenha identificado a maioria dos ataques, seus resultados foram menos favoráveis que os do Random Forest nas métricas de classificação consideradas.

Os falsos negativos são especialmente relevantes em segurança de redes porque representam ataques que não foram identificados pelo sistema. Os falsos positivos também importam: um número elevado de alertas incorretos pode aumentar a carga de trabalho de analistas e dificultar a priorização de incidentes reais.

Assim, os resultados não devem ser interpretados apenas pela quantidade total de acertos. A natureza e o custo dos erros também precisam ser considerados.

### 4.3. Tempo de treinamento e previsão

Os tempos registrados durante uma execução estão apresentados na Tabela 3.

**Tabela 3 — Tempos observados de execução.**

| Modelo | Treinamento | Previsão do conjunto de teste |
|---|---:|---:|
| Decision Tree | 11,88 s | 0,0141 s |
| Random Forest | 14,98 s | 0,0957 s |
| XGBoost | 0,54 s | 0,0183 s |

[Inserir os gráficos `comparacao_treinamento.png` e `comparacao_previsao.png`, usando os nomes reais dos arquivos gerados.]

O XGBoost apresentou o menor tempo de treinamento observado, aproximadamente 0,54 segundo. O Random Forest levou aproximadamente 14,98 segundos, enquanto a Decision Tree levou 11,88 segundos.

Na previsão do conjunto completo de teste, a Decision Tree apresentou o menor tempo observado, aproximadamente 0,0141 segundo. O XGBoost levou aproximadamente 0,0183 segundo, e o Random Forest, 0,0957 segundo.

Esses resultados mostram que o menor tempo de treinamento não implica necessariamente o menor tempo de previsão. Cada etapa possui custos computacionais diferentes, e o Random Forest precisa combinar as previsões de várias árvores.

Os tempos devem ser tratados como observações de uma execução específica. Eles podem variar conforme o equipamento, a carga do sistema, a configuração das bibliotecas e outros fatores. Para estabelecer uma comparação mais robusta, seria recomendável repetir as medições em condições controladas e reportar a mediana ou a média dos tempos observados.

### 4.4. Importância das características

A análise das características permite examinar quais variáveis receberam maior importância segundo os modelos.

No Random Forest, as características de maior importância foram:

| Característica | Importância aproximada |
|---|---:|
| `ct_state_ttl` | 0,1009 |
| `sttl` | 0,0797 |
| `sload` | 0,0653 |
| `rate` | 0,0462 |
| `dload` | 0,0431 |

[Inserir `importancia_random_forest.png`.]

No XGBoost, a característica `sttl` apresentou importância aproximada de 0,6654, muito superior às demais. Em seguida, destacaram-se `dbytes`, com aproximadamente 0,0530, e `ct_srv_dst`, com aproximadamente 0,0279.

[Inserir `importancia_xgboost.png`.]

A diferença entre os dois modelos é relevante. Enquanto o Random Forest distribuiu a importância entre diversas características, o XGBoost atribuiu uma parcela expressiva da importância a `sttl`. Essa característica representa o valor do TTL observado na direção de origem do tráfego, sendo relacionada ao comportamento dos pacotes na rede.

A árvore de decisão também utilizou `sttl` em sua primeira divisão, com o limiar 61. Essa coincidência sugere que a característica desempenhou um papel importante nas estruturas aprendidas pelos modelos avaliados.

Entretanto, as importâncias apresentadas são específicas dos algoritmos e de suas configurações. Uma importância elevada não significa que a característica, isoladamente, seja suficiente para detectar um ataque. Tampouco demonstra uma relação causal entre a variável e o comportamento malicioso. Uma investigação adicional, por exemplo por meio de importância por permutação e análise de erros por categoria, poderia aprofundar essa interpretação.

### 4.5. Síntese comparativa

Os resultados permitem resumir as principais diferenças observadas:

- **Decision Tree:** apresentou estrutura de decisão mais fácil de visualizar, menor tempo de previsão observado e métricas inferiores às do Random Forest.
- **Random Forest:** apresentou a maior acurácia, precisão e F1-score, além da menor quantidade de falsos positivos.
- **XGBoost:** apresentou o maior recall, a menor quantidade de falsos negativos e o menor tempo de treinamento observado.

Considerando o equilíbrio entre as métricas, o Random Forest foi o modelo com melhor resultado geral neste experimento. Por outro lado, se a prioridade principal for reduzir a quantidade de ataques não detectados, o XGBoost merece atenção especial.

Essa conclusão é condicionada ao conjunto de dados, às configurações utilizadas e ao procedimento experimental adotado. Não é possível afirmar que um algoritmo será superior em todos os cenários de detecção de intrusões.

## 5. Limitações do estudo

Embora os resultados permitam comparar os modelos no cenário avaliado, algumas limitações precisam ser reconhecidas.

Primeiramente, a distribuição das classes difere entre os conjuntos de treinamento e teste. Essa diferença pode influenciar as métricas observadas e deve ser considerada ao interpretar os resultados.

Em segundo lugar, os modelos não utilizaram configurações completamente equivalentes de ponderação das classes. A Decision Tree e o Random Forest foram treinados com `class_weight="balanced"`, enquanto o XGBoost não recebeu uma configuração equivalente. Portanto, parte das diferenças pode estar relacionada tanto ao algoritmo quanto às configurações adotadas.

Além disso, não foi realizada uma busca sistemática de hiperparâmetros. Os resultados representam as configurações selecionadas para este experimento, não necessariamente o melhor desempenho possível de cada algoritmo.

Os tempos de execução foram registrados em uma única execução apresentada na tabela. Repetições em condições controladas seriam necessárias para produzir estimativas mais estáveis do custo computacional.

A análise de importância das características também possui limitações. As importâncias internas dos algoritmos não são diretamente equivalentes entre si e não estabelecem causalidade. Para uma investigação mais aprofundada, poderiam ser utilizadas técnicas complementares de explicabilidade.

Por fim, o estudo utiliza um conjunto de dados público específico. O desempenho observado não garante os mesmos resultados em redes reais, ambientes com padrões de tráfego diferentes ou ataques que não estejam adequadamente representados no conjunto utilizado.

## 6. Conclusão

Este trabalho comparou os algoritmos Decision Tree, Random Forest e XGBoost na tarefa de detecção de intrusões em redes, utilizando o conjunto de dados UNSW-NB15 e avaliando métricas de classificação, tempos de execução, matrizes de confusão e importância das características.

O Random Forest apresentou o melhor equilíbrio geral entre as métricas analisadas, alcançando 89,29% de acurácia e F1-score de 90,93%. Também apresentou a maior precisão, de 85,19%, e a menor quantidade de falsos positivos entre os modelos avaliados.

O XGBoost alcançou o maior recall, de 98,70%, e apresentou 589 falsos negativos, indicando a menor quantidade de ataques não identificados. Além disso, teve o menor tempo de treinamento observado, de aproximadamente 0,54 segundo. Entretanto, apresentou mais falsos positivos que o Random Forest.

A Decision Tree teve desempenho inferior nas métricas gerais, mas oferece uma estrutura mais direta para visualizar e explicar regras de classificação. Essa característica pode ser relevante em situações nas quais a compreensão do processo decisório seja uma prioridade.

Em resposta à questão de pesquisa, conclui-se que não existe um único modelo superior em todos os critérios avaliados. O Random Forest foi o mais equilibrado nas métricas de classificação utilizadas, enquanto o XGBoost foi mais favorável à redução de ataques não identificados e ao tempo de treinamento observado. A Decision Tree destacou-se pela interpretabilidade direta de sua estrutura.

Como trabalhos futuros, recomenda-se realizar uma busca sistemática de hiperparâmetros, investigar configurações mais comparáveis para o tratamento das classes, repetir os testes de tempo em condições controladas e avaliar o comportamento dos modelos em outros conjuntos de dados. Também seria relevante examinar a importância das características com métodos complementares e analisar o desempenho por categoria de ataque.

Dessa forma, o estudo contribui para compreender as vantagens e limitações de diferentes algoritmos de classificação no contexto da segurança de redes, ressaltando que a escolha de um modelo deve considerar não apenas a taxa de acerto, mas também o custo dos erros, o desempenho computacional e as necessidades de interpretação.

## Referências

BREIMAN, Leo. Random Forests. *Machine Learning*, v. 45, p. 5–32, 2001. DOI: https://doi.org/10.1023/A:1010933404324.

CHEN, Tianqi; GUESTRIN, Carlos. XGBoost: A Scalable Tree Boosting System. In: *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. 2016. p. 785–794. DOI: https://doi.org/10.1145/2939672.2939785.

MOUSTAFA, Nour; SLAY, Jill. UNSW-NB15: a comprehensive data set for network intrusion detection systems (UNSW-NB15 network data set). In: *Military Communications and Information Systems Conference (MilCIS)*. 2015. DOI e dados bibliográficos completos devem ser conferidos na publicação original.

SCIKIT-LEARN DEVELOPERS. *DecisionTreeClassifier documentation*. Disponível em: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html. Acesso em: [data de acesso].

UNIVERSITY OF NEW SOUTH WALES. *The UNSW-NB15 Dataset*. Disponível em: https://research.unsw.edu.au/projects/unsw-nb15-dataset. Acesso em: [data de acesso].

## Autores

**Eduardo Quintino Filho** 

**Felipe Veiga da Silva** 

**Henrique de Aguiar Fernandes** 

**Niccolas Luppeti dos Santos** 

**Tharik de Lima Santos** 

## Repositório e reprodutibilidade

**Código-fonte:** https://github.com/FelipeVeiga775/Artigo_preditor_redes

**Dados utilizados:** Todos os dados estão presente na pasta "dados"

**Instruções de execução:** Clone o repositório, instale as dependências Python necessárias e execute os scripts de processamento, treinamento e avaliação dos modelos conforme documentado no projeto. Para visualizar o site localmente, abra o index.html com a extensão Live Server do VS Code.

**Data da última atualização:** 21/10/2026

