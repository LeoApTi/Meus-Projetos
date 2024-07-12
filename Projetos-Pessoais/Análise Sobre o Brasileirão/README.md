# Análise de Dados do Campeonato Brasileiro

## Objetivo
Mostrar alguns dados sobre o Campeonato Brasileiro de Futebol por meio da análise de um dataset do site Kaggle e desenvolver minhas habilidades técnicas, de resolução de problemas e pensamento crítico.

## Desenvolvimento
Para realizar esta tarefa, busquei responder as seguintes perguntas:

- Em quais minutos saem mais gols no geral? E por clube?
- Quantos gols cada time fez no total? Quantos foram de penalty? Quantos de bola rolando/parada? Quantos contra? Quantos gols a favor (retirando os gols contra)  no total?
- Quais os atletas, deste período, que mais fizeram gols? E quantos gols fizeram? Em qual clube estavam?
- Dado um respectivo clube, quais foram os atletas que fizeram mais gols?
- Qual foi a média de gols total durante esse período?

E para respondê-las, utilizei a biblioteca Pandas da linguagem de programação Python. Abaixo deixo alguns métodos usados:

- groupby(): mostra os valores de acordo com um determinado grupo
- query(): faz uma consulta no dataframe
- value_counts(): contagem de valores
- head(): mostra um determinado número de linhas
- read_csv(): ler um arquivo '.csv'
- sort_values(): ordenar os dados na ordem crescente ou decrescente

## Conclusão
Me diverti bastante utilizando a biblioteca Pandas pela primeira vez e percebi que ela é muito importante para analisar dados, muitas das vezes facilitando processos que demorariam bastante no excel.
