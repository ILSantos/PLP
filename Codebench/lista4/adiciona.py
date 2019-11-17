#!/usr/bin/python3 
""" 
Implemente uma função adiciona(L, x) que insere o elemento x ao final da lista L.

Não use o operador + do Python, nem métodos como append. 
"""
import sys

def adiciona(L, x):
    pass


##############################
# Nao modifique o programa daqui para baixo
casos = [(1, []),
        (2, [1]),
        (3, [1, 2]),
        ([1], []),
        (4, [1,2,3]),
        ([1,2],[[3], 4]),
        (1,[]),
        ([],[1,2,3]),
        (1, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
        (42, [1,[2,[3,[4,[5,[6],7],8],9],10]]),
        (11, [11, 12, 13, 31, 21]),
        ([5,4,3,2,1], [1,2,3,4,5])]

num = 0
for caso in casos:
    elemento = caso[0]
    lista = caso[1]

    lista_segura = lista.copy()
    if type(elemento) is list:
        elemento_seguro = elemento.copy()
    else:
        elemento_seguro = elemento

    saida_esperada = lista + [elemento]
    saida = adiciona(lista, elemento)

    if saida == saida_esperada:
        print("Caso #%d: ok!" % num)
    else:
        print("Caso #%d: erro" % num)
        print("  Entrada:")
        print("    Lista    =", lista_segura)
        print("    Elemento =", elemento_seguro)
        print("  Saida  esperada")
        print("   ", saida_esperada)
        print("   Saida obtida")
        print("   ", saida)
