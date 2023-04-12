# Contexto
A FlyFood é uma empresa que busca oferecer soluções inovadoras para otimização de entregas, utilizando drones capazes de transportar vários pedidos em seu
compartimento. No entanto, a limitação das baterias dos drones é um grande desafio que precisa ser superado para tornar essa solução viável.
Para enfrentar esse desafio, a empresa está desenvolvendo um algoritmo capaz de determinar a melhor rota para o drone realizar as entregas, levando em consideração
a duração da bateria, o ponto de origem, os pontos de entrega e o ponto de retorno do drone. O objetivo é garantir que todas as entregas possam ser realizadas dentro do ciclo de bateria do drone, reduzindo o tempo de deslocamento e minimizando o impacto ambiental causado pelos veículos convencionais. 

## Problema

O problema é definido por uma matriz onde os pontos de entrega são representados por A, B, C, D e o ponto de origem e retorno R. O drone só pode se mover na horizontal ou na vertical, e não pode se mover na diagonal. 

## Entrada
A entrada é fornecida através de um arquivo texto onde cada linha representa uma linha da matriz. Além disso, os pontos não válidos são representados por zero.

```
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
``` 

## Saída
O output é a ordem de entrega dos pacotes, representada por uma string, na qual a menor distância é percorrida.

## Autor

O projeto foi desenvolvido por mim para a disciplina de Projeto Interdisciplinar de Sistemas de Informação II, lecionada pelo professor Rodrigo Soares. Foi inteiramente feito em python, com auxílio da biblioteca matplotlib para criação de gráficos e experimentos.

## Links externos 
1. **[Descrição do problema](https://docs.google.com/document/d/1SC2B2q2Ue5bndAYnmT1o2L613gChXxNb/edit?usp=sharing&ouid=111358670991522502707&rtpof=true&sd=true)**
