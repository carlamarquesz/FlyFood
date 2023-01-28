import time
import itertools
inicio = time.time()
#Recebendo como entrada a matriz e separando seus pontos e coordenadas
file = open('matriz', 'r')
n, m = file.readline().split() 
linhas = file.read().splitlines()    
lista_coordenadas = []
lista_pontos = []   
for i in range(int(n)):
    linha = linhas[i].split()  
    for j in linha: 
        if j != '0':
            coordenada = (i, linha.index(j)) 
            lista_coordenadas.append(coordenada)
            lista_pontos.append(j)
indice = lista_pontos.index('R') 
ponto_R = lista_coordenadas[indice]
#print(ponto_R)
lista_coordenadas.remove(lista_coordenadas[indice]) 
lista_pontos.remove('R')   
#print('quantidade de pontos de entrega:', len(lista_pontos))
# Função permutação das minhas rotas possíveis
def permutacao(lista,qtd_pontos):
    permutacao = list(itertools.permutations(lista, qtd_pontos)) 
    return permutacao
# Função que calcula a distância entre os pontos de cada rota
distancias = []   
def calcular_distancias():
    coordenadas = permutacao(lista_coordenadas,len(lista_coordenadas))
    for i,pontos in enumerate(coordenadas): 
        pontos = list(pontos) 
        pontos.append(ponto_R) 
        posicao_atual = ponto_R 
        distancia_total = 0 
        #print(f'Rota {i+1}: {pontos}')    
        for ponto in pontos:  
            x = posicao_atual[0] - ponto[0]
            y = posicao_atual[1] - ponto[1] 
            dist_percorrida  = abs(x) + abs(y) 
            distancia_total += dist_percorrida 
            #print(f'Posição atual: {posicao_atual} Ponto: {ponto} Distância {dist_percorrida }') 
            posicao_atual = ponto 
        distancias.append(distancia_total)  
        #print(f'Distância total: {distancia_total}') 
    #print('quantidade de rotas:',i+1)
    return distancias
calcular_distancias()  
print('\n*** Caminho mínimo ***')
#Caminho mínimo dentre as rotas para efetuar a entrega 
for i, distancia in enumerate(distancias):  
    if distancia == min(distancias): 
        coordenadas = permutacao(lista_pontos,len(lista_pontos)) 
        print(f'Rota {i+1}: {list(coordenadas[i])}  Distância: {distancia}')   
fim = time.time()
print(f'Tempo de execução: {fim - inicio}')











