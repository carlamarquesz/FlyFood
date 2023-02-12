LISTA_PERMUTADA = []


def permute(lista, k, tamanho_lista):
    if k == tamanho_lista:
        LISTA_PERMUTADA.append(tuple(lista))
    else:
        for i in range(k, tamanho_lista):
            lista[k], lista[i] = lista[i], lista[k]
            permute(lista, k + 1, tamanho_lista)
            lista[k], lista[i] = lista[i], lista[k]
    return LISTA_PERMUTADA


def calcular_distancias(lista_coordenadas, ponto_R):
    distancias = []
    coordenadas = permute(lista_coordenadas, 0, len(lista_coordenadas))
    for i, pontos in enumerate(coordenadas):
        pontos = list(pontos)
        pontos.append(ponto_R)
        posicao_atual = ponto_R
        distancia_total = 0
        # print(f"Rota {i+1}: {pontos}")
        for ponto in pontos:
            x = posicao_atual[0] - ponto[0]
            y = posicao_atual[1] - ponto[1]
            dist_percorrida = abs(x) + abs(y)
            distancia_total += dist_percorrida
            # print(f'Posição atual: {posicao_atual} Ponto: {ponto} Distância {dist_percorrida }')
            posicao_atual = ponto
        distancias.append(distancia_total)
        # print(f'Distância total: {distancia_total}')
    # print('quantidade de rotas:',i+1)
    return distancias
