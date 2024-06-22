**Problema de Refeição Escolar**

## Descrição do Problema

O problema consiste em, dado um conjunto de ingredientes, gerar refeições para uma semana sendo cada refeição uma combinação de ingredientes. Um cardápio semanal deve satisfazer os requisitos nutricionais, ser variado e respeitar um orçamento.

## Objetivo

O objetivo é construir um algoritmo genético para resolver o problema através da avalição de diversos cardápios.

## Definição do AG

### Restrições

- Requisitos Nutricionais
- Orçamento
- Variabilidade

### Modelagem do Problema

- É definida uma lista de ingredientes, juntamente com suas respectivas informações nutricionais
- É definido o requisito nutricional de uma refeição
- É definido o orçamento para cada refeição

### Inicialização

É criada uma população inicial de tamanho arbitrário em que cada elemento representa o cardápio de uma semana.

### Avaliação

Utiliza-se uma função para calcular o fitness de cada cardápio considerando o quão distante o mesmo está dos valores nutricionais ideiais e seu custo.

### Variabilidade Genética

No crossover dois cardápios pais doam uma parte de suas refeições um para o outro.

Na mutação, um prato de um cardápio é substituído por outro.

### Critério de Parada

Após 250 gerações.