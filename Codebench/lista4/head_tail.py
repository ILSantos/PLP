#!/usr/bin/python3 
""" 
Faça uma função head(L) que retorna a cabeça da lista L e uma função tail(L) que retorna a cauda da lista L

A cabeça da lista é o primeiro elemento da lista. A função hd não precisa funcionar com uma lista vazia.

Exemplos:

head([1, 2, 3]) deve retornar 1;
head([1] deve retornar 1;
head([[1,2,3], [4, [5, 6]]]) deve retornar [1, 2, 3]
head([]) tem comportamento indefinido.
A cauda é uma lista que contém todos os elementos de L, exceto o primeiro. Note que uma lista vazia tem uma cauda vazia.
"""
import sys

def head(L):
    return L[0] # remova esta linha e insira seu codigo

def tail(L):
    return L[1:] # remova esta linha e insira seu codigo


##############################
# Nao modifique o programa daqui para baixo
casos = [dict(e=[1, 2, 3, 4], h=1, t=[2,3,4]),
    dict(e=[[1], [2, 3, 4]], h=[1], t=[[2,3,4]]),
    dict(e=[[1, 2], 3, 4], h=[1,2], t=[3,4]),
    dict(e=[[1, 2], [3], [4]], h=[1,2], t=[[3],[4]]),
    dict(e=[[[1], 2, 3], 3, 4, 5], h=[[1],2,3], t=[3,4,5]),
    dict(e=[1], h=1, t=[]),
    dict(e=[[1, 2]], h=[1,2], t=[]),
    dict(e=[[], 2, 3], h=[], t=[2,3]),
    dict(e=[[], []], h=[], t=[[]]),
    dict(e=[[]], h=[], t=[])]

for num in range(len(casos)):
    entrada = casos[num]['e']
    h_esperado = casos[num]['h']
    t_esperado = casos[num]['t']

    saida_h = head(entrada) == h_esperado
    saida_t = tail(entrada) == t_esperado

    if saida_h and saida_t:
        print("Caso #%d: ok!" % num)
    else:
        print("Caso #%d: erro" % num)
        print("  Etrada:", entrada)
        print("  Saida esperada:")
        print("    head:", h_esperado)
        print("    tail:", t_esperado)
        print("  Saida obtida:")
        print("    head:", saida_h)
        print("    tail:", saida_t)