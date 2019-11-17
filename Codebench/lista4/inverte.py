#!/usr/bin/python3 
""" 
Faça uma função inverte(L) que retorna a o inverso da lista L.

Não len, for ou list.reverse. 
"""
import sys

def inverte(L):
    return L[::-1]


##############################
# Nao modifique o programa daqui para baixo
casos = [[1, 2, 3, 4],
    [[1], [2, 3, 4]],
    [[1, 2], 3, 4],
    [[1, 2], [3]],
    [[[1], 2, 3]],
    [1],
    [[1, 2]],
    [[], 2, 3],
    [[], []],
    [[]]]

for num in range(len(casos)):
    entrada = casos[num]
    entrada_original = entrada.copy()

    saida_esperada = entrada.copy()
    saida_esperada.reverse()

    saida = inverte(entrada)

    if saida is entrada:
        print("Caso #%d: lista modificada!! Use recursao e nao altere o estado" % (num + 1))
    elif saida == saida_esperada:
        print("Caso #%d: ok!" % (num + 1))
    else:
        print("Caso #%d: erro" % (num + 1))
        print("  Entrada :", entrada_original)
        print("  Esperado:", saida_esperada)
        print("  Obtido  :", saida)