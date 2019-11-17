#!/usr/bin/python3 
""" 
Leia várias listas do teclado.
Utilizando funções lambda, map ou compreensões de listas, imprima uma lista contendo o quadrado de cada elemento 
da lista de entrada.

Entrada
A entrada conterá várias listas. Cada uma em uma linha. Faça a leitura com geradores e eval.

Saída
Imprima a lista em formato Python. Siga o exemplo inicial.

    Entrada:  [1]
              [2,3] 
    Saída:    [1] 

"""
import sys

for caso in map(eval, sys.stdin):
	# Modifique para imprimir a resposta correta. Se necessário declare funções adicionais
	resposta = [x ** 2 for x in caso] 
	print(resposta)



