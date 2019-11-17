#!/usr/bin/python3 
"""
Faça uma função qsort(L) que ordena uma lista de elementos distintos utilizando o método de ordenação quicksort.

O método da ordenação quicksort é baseado nos seguintes passos:

Selecione um pivô
Particione a lista de modo que todos os elementos à esquerda do pivô sejam menores ou iguais a ele e todos os elementos à direita do pivô sejam maiores ou iguais a ele
Ordene recursivamente as metades à esquerda e à direita do pivô
Essa apresentação tradicional do algoritmo, entretanto, pressupõe que a lista será modificada.

No paradigma funcional, uma abordagem semelhante consiste nos seguintes passos:

Selecione um pivô
Selecione a lista dos elementos menores que o pivô
Selecione a lista dos elementos maiores que o pivô
Ordene recursivamente as duas listas e faça a concatenação adequada de todos os elementos

Por exemplo, para ordenar a lista L=(4,5,3,1,2,7,6,8), se o pivô escolhido for 4, então a lista dos menores será E=(3,1,2) e a lista dos maiores 
será D=(5,7,6,8). Ordenando cada uma dessas listas recursivamente, obtemos as listas E′=(1,2,3), o pivô 4 e a lista D′=(5,6,7,8). Concatenando 
esses três elementos corretamente obtemos a lista ordenada.

Importante: não modifique a lista para o particionamento e não use laço de repetição para selecionar as sub-listas. Em vez disso, use filtros e 
maps ou compreensões de listas. 
"""
import sys

def qsort(L):
    if L == []:
        return []
    else:
        pivo = L[0]
        menor = qsort([x for x in L[1:] if x  < pivo])
        maior = qsort([x for x in L[1:] if x >= pivo])
        return menor + [pivo] + maior

##############################
# Nao modifique o programa daqui para baixo
from itertools import permutations
from numpy import random

r = random.RandomState(42)

casos = list(permutations(range(1, 5)))
casos += (list(permutations([1,2,5,8,10])))
casos.append(r.permutation(100))
casos.append(r.permutation(100))
casos.append(r.permutation(100))
casos.append(r.permutation(100))
casos.append(r.permutation(100))
casos.append(r.permutation(100))

print("Testando %d casos..." % len(casos))
num = 0
notificacoes = 0
acertos = 0
for caso in casos:
    entrada = list(caso)
    entrada_segura = entrada.copy()

    saida = qsort(entrada)

    saida_esperada = entrada.copy()
    saida_esperada.sort()

    num += 1
    if saida == saida_esperada:
        acertos += 1
    elif saida != saida_esperada:
        print("Caso #%d: erro!" % num)
        notificacoes += 1
        if notificacoes > 5:
            print("Muitos erros! Desisto!")
            break
        else:
            print("  Entrada :", entrada_segura)
            print("  Esperado:", saida_esperada)
            print("  Obtido  :", saida)

if acertos == len(casos):
    print("Todos os casos corretos!")