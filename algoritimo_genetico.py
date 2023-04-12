import random, time, math
import matplotlib.pyplot as plt

# Define os parâmetros do algoritmo genético
tamanho_populacao = 10  # quantos indivíduos vão ser gerados em cada geração.
taxa_mutacao = 0.01
geracoes = 100

# Inicializando meu programa e obtendo a minha matriz
with open("matriz", "r") as f:
    linhas = f.readlines()[1:]
matrix = []
for linha in linhas:
    linha = linha.strip().split()
    matrix.append(linha)

# Cria uma lista e um dicionario com os pontos diferentes de zero
pontos = []
dict_pontos = []
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if str(matrix[i][j]) != "0" and matrix[i][j] != "R":
            pontos.append(matrix[i][j])
            dict_pontos.append({"x": i, "y": j, "name": matrix[i][j]})
        if matrix[i][j] == "R":
            posicao_R = {"x": i, "y": j, "name": matrix[i][j]}

# Função para calcular a aptidão da população utilizando a função fitness.
def aptidao(populacao):
    lista_apitidoes = [None] * len(populacao)
    for i, individuo in enumerate(populacao):
        lista_apitidoes[i] = fitness(individuo)
    maximo = sum(lista_apitidoes)
    return [maximo - x for x in lista_apitidoes]


def fitness(individuo):
    # Calcula a distância entre a posição R e o primeiro ponto do indivíduo
    distancia_total = abs(posicao_R["x"] - dict_pontos[individuo[0]]["x"]) + abs(
        posicao_R["y"] - dict_pontos[individuo[0]]["y"]
    )
    # Para cada par de pontos consecutivos no indivíduo, calcula a distância entre eles e adiciona à distância total
    for i, ponto_atual in enumerate(individuo):
        if i != len(individuo) - 1:
            distancia_total += abs(
                dict_pontos[ponto_atual]["x"] - dict_pontos[individuo[i + 1]]["x"]
            ) + abs(dict_pontos[ponto_atual]["y"] - dict_pontos[individuo[i + 1]]["y"])
    # Calcula a distância entre a posição R e o último ponto do indivíduo, e adiciona à distância total
    distancia_total += abs(posicao_R["x"] - dict_pontos[individuo[-1]]["x"]) + abs(
        posicao_R["y"] - dict_pontos[individuo[-1]]["y"]
    )
    # Retorna a distância total calculada
    return distancia_total


# Esta função é responsável por selecionar os indivíduos mais aptos de uma população.
# A seleção é feita por meio de um torneio
def selection(populacao):
    lista_apt = aptidao(populacao)
    lista_pais = [None] * len(populacao)
    for i in range(0, len(populacao), 2):
        pai1 = torneio(lista_apt)
        pai2 = torneio(lista_apt)
        lista_pais[i], lista_pais[i + 1] = populacao[pai1], populacao[pai2]
    return lista_pais

def torneio(lista_apt):
    ind1 = random.randint(0, len(lista_apt) - 1)
    ind2 = ind1
    while ind1 == ind2:
        ind2 = random.randint(0, len(lista_apt) - 1)
    return ind1 if lista_apt[ind1] > lista_apt[ind2] else ind2

# Realiza o cruzamento genético entre dois indivíduos representados como listas retornando o filho.

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


# Percorrerá cada posição do indivíduo e, com uma probabilidade de 1%, trocará o valor dessa posição com o valor de outra posição aleatória (j).
def mutation(individuo):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            j = random.randint(0, len(individuo) - 1)
            individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo


# Cria a população inicial com indivíduos aleatórios.
def population(tamanho_populacao, pontos):
    populacao = []
    individuos_gerados = []
    # if tamanho_populacao > math.factorial(len(pontos)): tamanho_populacao = math.factorial(len(pontos))
    while len(populacao) < tamanho_populacao:
        individuo = list(range(len(pontos)))
        random.shuffle(individuo)
        if individuo not in individuos_gerados:
            populacao.append(individuo)
    return populacao


# Executa o algoritmo genético utilizando as funções de seleção, cruzamento e mutação para criar uma nova população em cada geração. 
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
pop = algoritmo_genetico(geracoes, tamanho_populacao, pontos)
lista_apt = aptidao(pop)
melhor_individuo = pop[lista_apt.index(max(lista_apt))]
rota = [pontos[i] for i in melhor_individuo]
distancia = fitness(melhor_individuo)
end = time.time()
print(f"Rota:{rota} \nDistância: {distancia}\nTempo de execução: {end-start}")


# # Gráfico da melhor rota
# rota_coordenada = [dict_pontos[i] for i in melhor_individuo]
# coordenadas_melhor_rota = (
#     [(posicao_R["x"], posicao_R["y"])]
#     + [(ponto["x"], ponto["y"]) for ponto in rota_coordenada]
#     + [(posicao_R["x"], posicao_R["y"])]
# ) 
# fig = plt.figure()
# plt.scatter(
#     [x for x, y in coordenadas_melhor_rota], [y for x, y in coordenadas_melhor_rota]
# )
# plt.plot(
#     [x for x, y in coordenadas_melhor_rota], [y for x, y in coordenadas_melhor_rota]
# )
# # Adicionar rótulos dos pontos
# for ponto in rota_coordenada:
#     plt.annotate(ponto["name"], (ponto["x"], ponto["y"]))
# plt.grid()
# plt.show()

# #Grafico comparação força bruta Vs AG 
# x = [4,5,7,8,10]
# y = [0.000971, 0.009004, 0.429994, 20.49354,60]
# y1 = [ 0.005997,0.006075,0.073047,0.079922,0.275868]
# plt.plot(x, y, label = 'Algoritmo força bruta')  
# plt.plot(x, y1, label = 'Algoritmo genético')
# plt.xlabel('Número de pontos de entrega')   
# plt.ylabel('Tempo de execução em segundos')   
# plt.title('Desempenho Força Bruta x Genético')   
# plt.legend()
# plt.savefig('forca-brutavsgenetico.png', format='png')
# plt.grid()
# plt.show() 