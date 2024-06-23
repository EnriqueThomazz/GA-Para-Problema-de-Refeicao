# Valores nutricionais base de uma refeição
qtd_por_ref = {"calorias": 650, "proteinas": 30, "ferro": 7, "zinco": 5, "vitamina A": 300}


# Tamanho do Cardápio em dias da semana
tam_cardapio = 7


# Orçamentos
custo_refeicao = 5
orcamento = tam_cardapio * custo_refeicao


# Ingredientes a serem evitados e a respectiva penalização
ingr_evitados = ["Salsicha", "Beterraba"]
penalizacao = 200


# Maior fitness teorico para um cardapio
maior_fitness_teorico = 10000


# Tamanho da população
tam_pop = 50


# Probabilidades de mutação e crossover
rate_mutacao = 0.4
rate_crossover = 0.4