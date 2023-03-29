import random, time, math
import matplotlib.pyplot as plt
 
# Inicializando meu programa e obtendo a minha matriz

with open("matriz", "r") as f:
    linhas = f.readlines()[1:]
matrix = []
for linha in linhas:
    linha = linha.strip().split()
    matrix.append(linha)


# Cria a lista com os pontos diferentes de zero
pontos = []
coordenada_r = None

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if str(matrix[i][j]) != "0":
            pontos.append(matrix[i][j])
        if matrix[i][j] == "R":
            coordenada_r = (i, j)  
pontos.remove("R") 

# Define os parâmetros do algoritmo genético
tamanho_populacao = 100  # quantos indivíduos vão ser gerados em cada geração.
tamanho_elite = 10
taxa_mutacao = 0.01
geracoes = 200


# A função fitness recebe um indivíduo, que é uma lista de índices que representam os pontos
# que devem ser visitados em uma determinada ordem. Essa função calcula a distância total percorrida pelo indivíduo
 
def fitness(individuo,imprimir_coordenadas=False):
    lista = ["R"] + [pontos[i] for i in individuo] + ["R"] 
    coordenada = [] 
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
                coordenada.append((x1,y1))
            if ponto2 in linha_matriz:
                x2 = indice
                y2 = linha_matriz.index(ponto2) 
            if x1 is not None and y2 is not None:
                break 
        distancia += abs(x1 - x2) + abs(y1 - y2)  # distancia de manhattan
    if imprimir_coordenadas:
        coordenada = coordenada + [coordenada_r]  
    return distancia, coordenada


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
    individuos_gerados = [] 
    #if tamanho_populacao > math.factorial(len(pontos)): tamanho_populacao = math.factorial(len(pontos))
    while len(populacao) < tamanho_populacao:
        individuo = list(range(len(pontos)))
        random.shuffle(individuo)
        if individuo not in individuos_gerados:
            populacao.append(individuo) 
    return populacao   
# Executa o algoritmo genético utilizando as funções de seleção, cruzamento e mutação para criar uma nova população em cada geração.
# Com um número maior de gerações, o algoritmo terá mais chances de encontrar uma solução ótima ou próxima da ótima
def algoritmo_genetico(geracoes, tamanho_populacao, pontos):
    populacao_inicial = population(tamanho_populacao, pontos)
    for i in range(geracoes):
        populacao = selection(populacao_inicial)
        nova_populacao = []
        while len(nova_populacao) < tamanho_populacao:
            pai1 = random.choice(populacao)
            pai2 = random.choice(populacao)
            filho = crossover(pai1, pai2)
            filho = mutation(filho)
            nova_populacao.append(filho)
        populacao_inicial = nova_populacao
    return populacao


# Encontra o melhor indivíduo com menor valor de fitness
start = time.time()
melhor_individuo = min(
    algoritmo_genetico(geracoes, tamanho_populacao, pontos), key=lambda x: fitness(x)
)
# Imprime o resultado
rota = [pontos[i] for i in melhor_individuo]
distancia, coordenada = fitness(melhor_individuo,imprimir_coordenadas=True)
end = time.time()
print("Melhor caminho: ", "-".join(rota))
print("Distância total: ", distancia)
print("Tempo de execução: ", end - start)
  
 
# # Gráfico da melhor rota
# fig = plt.figure() 
# plt.scatter([x for x, y in coordenada], [y for x, y in coordenada]) 
# plt.plot([x for x, y in coordenada], [y for x, y in coordenada])
# plt.grid() 
# plt.show()

# #Grafico comparação força bruta Vs AG
# x = [4,5,7,8,10]
# y = [0.000971, 0.009004, 0.429994, 20.49354,60]
# y1 = [0.81996,0.882999,1.519031,1.97299,3.25859]
# plt.plot(x, y, label = 'Algoritmo força bruta')  
# plt.plot(x, y1, label = 'Algoritmo genético')
# plt.xlabel('Número de pontos de entrega')   
# plt.ylabel('Tempo de execução em segundos')   
# plt.title('Desempenho Força Bruta x Genético')   
# plt.legend()
# plt.savefig('forca-brutavsgenetico.png', format='png')
# plt.grid()
# plt.show() 