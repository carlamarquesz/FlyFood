import random, time

# Inicializando meu programa e obtendo a minha matriz: [['0', '0', '0', '0', 'D'], ['0', 'A', '0', '0', '0'], ['0', '0', '0', '0', 'C'], ['R', '0', 'B', '0', '0']]

with open("matriz", "r") as f:
    linhas = f.readlines()[1:]
matrix = []
for linha in linhas:
    linha = linha.strip().split()
    matrix.append(linha)


# Cria a lista com os pontos diferentes de zero: ['D', 'A', 'C', 'R', 'B']
pontos = []
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if str(matrix[i][j]) != "0":
            pontos.append(matrix[i][j])
pontos.remove("R")

# Define os parâmetros do algoritmo genético
tamanho_populacao = 100  # quantos indivíduos vão ser gerados em cada geração.
tamanho_elite = 10
taxa_mutacao = 0.1
geracoes = 200


# A função fitness recebe um indivíduo, que é uma lista de índices que representam os pontos
# que devem ser visitados em uma determinada ordem. Essa função calcula a distância total percorrida pelo indivíduo


def fitness(individuo):
    lista = ["R"] + [pontos[i] for i in individuo] + ["R"]
    distancia = 0
    for i in range(0, len(lista) - 1):
        ponto1 = lista[i]  # primeira coordenada
        ponto2 = lista[i + 1]  # segunda coordenada
        x1, y1 = None, None
        x2, y2 = None, None
        for indice, linha_matriz in enumerate(
            matrix
        ):  # vai iterar sob cada linha da matriz com seu indice
            if ponto1 in linha_matriz:
                x1 = indice
                y1 = linha_matriz.index(ponto1)
            if ponto2 in linha_matriz:
                x2 = indice
                y2 = linha_matriz.index(ponto2)
            if x1 is not None and y2 is not None:
                break
        distancia += abs(x1 - x2) + abs(y1 - y2)  # distancia de manhattan
    return distancia


# Esta função é responsável por selecionar os indivíduos mais aptos de uma população.
# A seleção é feita por meio de um torneio


def selection(populacao):
    tamanho_torneio = 5
    selecionados = []
    for i in range(tamanho_elite):
        selecionados.append(populacao[i])
    for i in range(tamanho_populacao - tamanho_elite):
        torneio = random.sample(populacao, tamanho_torneio)
        melhor = min(torneio, key=lambda x: fitness(x))
        selecionados.append(melhor)
    return selecionados


# Realiza o cruzamento genético entre dois indivíduos representados como listas.
# a função retorna a lista "filho" resultante do cruzamento genético entre os dois pais.


def crossover(pai1, pai2):
    ponto_corte1 = random.randint(0, len(pai1) - 1)
    ponto_corte2 = random.randint(0, len(pai1) - 1)
    if ponto_corte1 > ponto_corte2:
        ponto_corte1, ponto_corte2 = ponto_corte2, ponto_corte1
    filho = pai1[ponto_corte1:ponto_corte2]
    for i in pai2:
        if i not in filho:
            filho.append(i)
    return filho


# Percorrerá cada posição do indivíduo e, com uma probabilidade de 10%, trocará o valor dessa posição com o valor de outra posição aleatória (j).
def mutation(individuo):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            j = random.randint(0, len(individuo) - 1)
            individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo


# Cria a população inicial: São as minhas rotas com seus respectivos indices
def population(tamanho_populacao, pontos):
    populacao = []
    for i in range(tamanho_populacao):
        individuo = list(range(len(pontos)))
        random.shuffle(individuo)  # embaralha aleatoriamente as 100 populacoes
        populacao.append(individuo)
    return populacao


# Executa o algoritmo genético utilizando as funções de seleção, cruzamento e mutação para criar uma nova população em cada geração.
# Com um número maior de gerações, o algoritmo terá mais chances de encontrar uma solução ótima ou próxima da ótima
def algoritmo_genetico(geracoes, tamanho_populacao, pontos):
    for i in range(geracoes):
        populacao = selection(population(tamanho_populacao, pontos))
        nova_populacao = []
        while len(nova_populacao) < tamanho_populacao:
            pai1 = random.choice(populacao)
            pai2 = random.choice(populacao)
            filho = crossover(pai1, pai2)
            filho = mutation(filho)
            nova_populacao.append(filho)
        populacao = nova_populacao
    return populacao


# Encontra o melhor indivíduo com menor valor de fitness
start = time.time()
melhor_individuo = min(
    algoritmo_genetico(geracoes, tamanho_populacao, pontos), key=lambda x: fitness(x)
)
# Imprime o resultado
rota = [pontos[i] for i in melhor_individuo]
distancia = fitness(melhor_individuo)
end = time.time()
print("Melhor caminho: ", "-".join(rota))
print("Distância total: ", distancia)
print("Tempo de execução: ", end - start)
