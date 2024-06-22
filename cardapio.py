import random
from ingredientes import ingredientes
from config import *

# Inicialização
def criaRefeicao():
    # Seleciona 2 essenciais, 1 proteína e 3 saladas
    refeicao = []

    essenciais = []
    carne = []
    saladas = []
    for ing in ingredientes:
        if ing['tipo'] == 'E':
            essenciais.append(ing)
        elif ing['tipo'] == 'P':
            carne.append(ing)
        elif ing['tipo'] == 'S':
            saladas.append(ing)

    refeicao += random.sample(essenciais, 2) + random.sample(carne, 1) + random.sample(saladas, 3)

    # Calculando o valor nutricional e custo
    calorias = 0
    proteinas = 0
    ferro = 0
    zinco = 0
    vit_a = 0
    custo = 0
    for ing in refeicao:
        calorias += ing['calorias']
        proteinas += ing['proteinas']
        ferro += ing['ferro']
        zinco += ing['zinco']
        vit_a += ing['vitamina A']
        custo += ing['custo']

    valor_nutricional = {"calorias": calorias, "proteinas": proteinas, "ferro": ferro, "zinco": zinco, "vitamina A": vit_a, "custo": custo}

    return {"refeicao": refeicao, "valor_nutricional": valor_nutricional}


def criaCardapio():
    cardapio = []

    for _ in range(7): cardapio.append(criaRefeicao())

    return cardapio

# Função de Avaliação
def fitnessCardapio(cardapio):
    # Quanto menor a fitness, mais adequado é
    dif = 0
    ing_rep = []
    for refeicao in cardapio:
        for nut in list(qtd_por_ref.keys()):
            # Calcula o quão distante (em módulo) os nutrientes do prato estão do valor nutricional desejado
            dif += abs(refeicao["valor_nutricional"][nut] - qtd_por_ref[nut])

        # Adiciona à dif o custo do prato
        dif += refeicao["valor_nutricional"]["custo"]

        # Verifica repetições, adiciona cada elemento único na lista
        for ingr in refeicao["refeicao"]:
            if ingr["nome"] not in ing_rep:
                ing_rep.append(ingr["nome"])

    # Fitness calculada como o grau de diferença mais a qtd de ingredientes repetidos (quanto maior a lista de ingr_rep, melhor)

    fitness = dif + 7 * (2 + 1 + 3) - len(ing_rep)

    return fitness


# Variabilidade Genética
def mutacao(pop):

    # Mutação de refeicao
    for i in range(len(pop)):
        # Probabilidade de mutação
        if random.choices([1, 0], [rate_mutacao, 1-rate_mutacao], k=1):
            # Substituindo um prato aleatório do cardapio mutante por outro
            pop[i][random.choice(range(0, len(pop[i])))] = criaRefeicao()


def crossover(pop):
    # Seleciona dois cardapios aleatorios
    index_pais = []

    for i in range(len(pop)):
        # Probabilidade de crossover
        if random.choices([1, 0], [rate_crossover, 1-rate_crossover], k=1):
            # Joga o cardapio na lista de pais
            index_pais.append(i)

    # Se não tiver um casamento perfeito de pares de pais, remove um elemento
    if len(index_pais) % 2 != 0:
        index_pais.pop(0)


    for i in range(0, len(index_pais), 2):
        pai1 = index_pais[i]
        pai2 = index_pais[i+1]

        # Definindo a proporção do crossover, pode ser nas proporções 1:6, 2:5, 3:4, 4:3, 5:2 e 6:1
        slice = random.randint(1, len(pop[pai1])-1)

        # Executando o crossover de fato
        pop[pai1], pop[pai2] = pop[pai1][:slice] + pop[pai2][slice:], pop[pai2][:slice] + pop[pai1][slice:]


def start():
    # Gera populacao inicial
    populacao = []
    for _ in range(tam_pop): populacao.append(criaCardapio())

    # Iterações
    for gen in range(250):
        # Calcula fitnesses
        fitnesses = []
        for cardapio in populacao:
            fitnesses.append(maior_fitness_teorico - fitnessCardapio(cardapio))

        # Seleção, método roleta, todos os individuos tem uma probabilidade com base no fitness de serem escolhidos
        populacao = random.choices(populacao, fitnesses, k=tam_pop)

        # Variabilidade Genética
        crossover(populacao)
        mutacao(populacao)

    # Melhor cardápio
    fitnesses = []
    for cardapio in populacao:
        fitnesses.append(maior_fitness_teorico - fitnessCardapio(cardapio))

    melhor_cardapio = populacao[fitnesses.index(max(fitnesses))]

    print(melhor_cardapio)

    print("\n\n\n")
    
    print(max(fitnesses))
    
    return melhor_cardapio


start()


# Coisas interessantes a serem implementados (???)

# Permitir uma escolha fracionária de ingredientes
# Permitir uma penalização para ingredientes (no caso de alguma pessoa não comer alguma coisa)

# Coisas a fazer (!!!)

# Permitir uma mutação a nível de ingrediente
# Brincar com os rates de mutação e crossover e ver como isso impacta no resultado