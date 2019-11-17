#!/usr/bin/python3 
""" 
Faça uma função palindromo(L) que retorna True se a lista L é um palíndromo e False caso contrário.

Uma lista é um palíndromo se ela pode ser lida da mesma forma nos dois sentidos.

Exemplos de palíndromos:

[1, 2, 3, 2, 1]
['a', 'b', 'b', 'a']
[True]
[]
Exemplos que não são palíndromos:

[1, 2, 3, 4]
['ab', 'ba']
[[1, 2], 3, 2, 1] 
"""
import sys

def palindromo(L):
    if L == L[::-1]:
        return True
    else:
        return False


##############################
# Nao modifique o programa daqui para baixo
casos = [[1,2,3],
        [1,2,3,2,1],
        [[1], 1],
        [1],
        [[],[1,2,3]],
        [[]],
        [],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1],
        [1,[2,[3,[4,[5,[6],4],3],2],1]],
        [11, 12, 13, 31, 21, 11],
        [[1,2,3,4,5]],
        [[1,2,3,4,5],[5,4,3,2,1]],
        [[1,2,3,4,5],[1,2,3,4,5]]]

num = 0
for caso in casos:
    entrada = caso.copy()
    entrada_segura = entrada.copy()
    
    reverso = entrada.copy()
    reverso.reverse()
    
    saida = palindromo(entrada)
    saida_esperada = entrada_segura == reverso

    num += 1
    if saida is entrada:
        print("Caso #%d: lista modificada!! Use recursao e nao altere o estado" % num)
    elif saida == saida_esperada:
        print("Caso #%d: ok!" % num)
    else:
        print("Caso #%d: erro" % num)
        print("  Entrada :", entrada_segura)
        print("  Esperado:", saida_esperada)
        print("  Obtido  :", saida)