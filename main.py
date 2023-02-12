import time
from utils import calcular_distancias, permute

inicio = time.time()

# Recebendo como entrada a matriz e separando seus pontos e coordenadas
file = open("matriz", "r")
n, m = file.readline().split()
linhas = file.read().splitlines()
lista_coordenadas = []
lista_pontos = []
for i in range(int(n)):
    linha = linhas[i].split()
    for j in linha:
        if j != "0":
            coordenada = (i, linha.index(j))
            lista_coordenadas.append(coordenada)
            lista_pontos.append(j)
indice = lista_pontos.index("R")
ponto_R = lista_coordenadas[indice]
lista_coordenadas.remove(lista_coordenadas[indice])
lista_pontos.remove("R")

# Caminho mínimo dentre as rotas para efetuar a entrega
distancias = calcular_distancias(lista_coordenadas, ponto_R)
print("\n*** Caminho mínimo ***")
for i, distancia in enumerate(distancias):
    if distancia == min(distancias):
        nomes_pontos = []
        pontos_permutados = permute(lista_coordenadas, 0, len(lista_coordenadas))[i]
        for ponto in pontos_permutados:
            nomes_pontos.append(lista_pontos[lista_coordenadas.index(ponto)])
        print(f"Rota {i+1}: {nomes_pontos}  Distância: {distancia}")
fim = time.time()
print(f"Tempo de execução: {fim - inicio}")
