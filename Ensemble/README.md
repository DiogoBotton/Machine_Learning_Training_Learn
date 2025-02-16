### Métodos de Ensemble

**Ensemble Learning** é uma abordagem em Machine Learning que busca combinar múltiplos modelos para criar um sistema mais robusto e eficaz. A ideia por trás dos métodos de ensemble é:
- Em vez de depender de um único modelo para fazer previsões, vários modelos são treinados e sesu resultados são combinados de forma a produzir uma resposta final que considera a contribuição de cada um.
- Modelos de ensemble podem gerar modelos preditivos com menos viés e menor variância ao combinar as forças de múltiplos modelos individuais.

#### Bagging

Bagging (Boostrap Aggregating) é uma técnica de ensemble que melhora a estabilidade e precisão de modelos. A ideia central do bagging é treinar vários modelos independentes em subconjuntos aleatórios de dados e combinar suas previsões.

**Como funciona?**
- O conjunto de dados original é dividido em vários subconjuntos por meio do bootstrap, criando múltiplas versões do dataset.
- Um modelo é treinado em cada subconjunto, podendo ser o mesmo tipo de algoritmo ou diferentes tipos.
- As previsões dos modelos são combinadas: em problemas de regressão, a média das previsões é usada; em problemas de classificação a combinação é realizada por **votação majoritária** (o resultado mais frequente é escolhido).

**Exemplos de técnicas de Bagging:**
- **Random Forest** é um dos exemplos mais populares de bagging. Onde ele utiliza várias árvores de decisão como modelos base e ao final, realiza a votação para retornar o resultado mais frequente como resposta do modelo.
- **BaggingClassifier** ou **BagginRegressor** pode ser utilizado para aplicar o bagging a qualquer algoritmo de base. Por exemplo, pode-se criar um ensemble de modelos de regressão linear ou KNN, e as previsões serão a média ou votação dos resultados individuais.

#### Boosting

Boosting é uma técnica de ensemble que melhora o desempenho de modelos de Machine Learning ao combinar vários modelos fracos em um modelo forte. Ao contrário do bagging, onde os modelos são treinados de forma independente, **no boosting os modelos são treinados sequencialmente, e cada novo modelo é ajustado para corrigir os erros dos modelos anteriores.** Essa abordagem foca em aprender com os carros, criando um modelo mais preciso a cada iteração.

![single_bagging_boosting](img/image.png)

**Como funciona?**
- Inicialmente, o primeiro modelo é treinado com pesos iguais para todas as observações.
- Em seguida, os dados nos quais o primeiro modelo cometeu erros recebem maior peso ou atenção.
- Um novo modelo é treinado levando em conta essas observações passadas, e suas previsões são combinadas com as do modelo anterior.
- Esse processo continua, com cada novo modelo focando em corrigir os erros acumulados pelos anteriores.
- No final, as previsões de todos os modelos são combinadas para formar a previsão final, frequentemente ponderada com base na precisão de cada modelo (da mais importância ou peso às previsões de modelos que apresentam melhor desempenho).

**Exemplos de técnicas de Boosting**
- **AdaBoost (Adaptive Boosting)**: O primeiro modelo é treinado e seus erros são identificados. Ems eguida o segundo modelo foca em corrirgir esses erros dando mais peso às observações que foram mal classificadas pelo primeiro modelo. Esse processo continua até que um número pré-definido de modelos seja criado. No final, as previsões são combinadas, geralmente com uma votação ponderada para classificação ou uma média ponderada para regressão. AdaBoost é conhecido por melhorar a precisão de modelos de classificação, especialmente em problemas onde os dados são lineares.
- **Gradient Boosting** e **XGBoost (Extreme Gradient Boosting)**: Nessa técnica, cada novo modelo é treinado para minimizar o erro residual (a diferença entre as previsões e os valores reais) dos modelos anteriores. Isso é feito de forma incremental, onde cada novo modelo tenta reduzir o erro do modelo anterior. O XGBoost é uma versão otimizada do Gradient Boosting, porém inclui melhorias de performance e velocidade, como regularização adicional para reduzir o overfitting.

#### Voting

Voting é uma técnica de ensemble que **combina as previsões de múltiplos modelos diferentes para gerar uma única previsão final**, de modo a aumentar a robustez e a precisão do modelo preditivo. Ao contrário do bagging e do boosting, em que geralmente se usa o mesmo tipo de modelo repetidamente (como múltiplas árvores de decisão), **o voting permite combinar diferentes algoritmos**, como uma combinação de modelos de árvore de decisão, regressão logística e KNN, para tirar proveito das forças de cada um.

![voting](img/image-1.png)

**Como funciona?**
- **Voting Majoritário (Hard Voting)**: Nesse método, cada modelo gera uma previsão de classe para uma instância, e a classe que receber mais votos é a escolhida como previsão final.
- **Voting Ponderado (Soft Voting)**: Esse método leva em consideração as probabilidades preditivas de cada modelo. Cada modelo calcula a probabilidade de uma instância pertencer a cada classe, e a previsão final é feita com base na média dessas probabilidades ponderadas. Essa abordagem é útil quando alguns modelos são mais confiáveis que outros, permitindo que se atribuam pesos diferentes para cada modelo. Assim, modelos mais precisos podem ter maior influÊncia na decisão final.

#### Stacking

Stacking é uma técnica de ensemble que **combina as previsões de múltiplos modelos** (também chamados de "nível zero") **usand um modelo adicional** (chamado de "nível 1" ou "meta-modelo") **para fazer a previsão final**. Ao contrário de métodos como bagging ou boosting, em que as previsões de múltiplos modelos são combinadas diretamente (por votação ou média), o **stacking permite que o modelo de segundo nível aprenda como combinar as previsões dos modelos iniciais de forma mais sofisticada**.

**Como funciona?**
- **Nível Zero (Modelos Base)**: Vários modelos base são treinados no conjunto de dados original. Esses modelos podem ser de diferentes tipos, como árvores de decisão, regressão logística ou KNN, cada um com suas próprias características e pontos fortes.
- **Geração de Previsões para o Meta-Modelo**: Depois que os modelos de primeiro nível são treinados, **suas previsões para cada instância no conjunto de dados são salvas**. Em vez de fazer previsões diretamente no conjunto de teste, o stacking utiliza as previsões dos modelos de nível zero como features para o próximo modelo. Isso cria um novo conjunto de dados, onde cada coluna representa as previsões de um modelo base.
- **Nível 1 (Meta-Modelo)**: Um novo modelo é treinado usando as previsões dos modelos base como entradas. Esse meta-modelo aprende a combinar as previsões iniciais de forma a minimizar o erro final. O meta-modelo é, muitas vezes, um algoritmo simples, como uma regressão linear ou uma árvore de decisão, mas pode ser qualquer modelo que se adapte bem ao problema.