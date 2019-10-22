#!/usr/bin/python3 

""" 
Escreva uma função que remove todos os zeros de uma lista de valores inteiros. Sua função deve 
receber uma lista e retornar a lista resultante da operação.Por exemplo, se o vetor de original 
contiver os inteiros 1,−1,2,0,3,0,4, então o vetor resultante deve conter os elementos 1,−1,2,3,4.
Faça um programa principal que lê um vetor e imprime o vetor resultante da sua função.

Entrada
Haverá vários casos de teste.Cada caso de teste começa com um inteiro N, indicando o número de valores 
do vetor (0<N<100). Os N valores seguintes serão os inteiros do vetor. Todos os valores são separados 
por espaços ou quebras-de-linha.O fim da entrada é indicado pelo sentinela N=0.

Saída
Para cada caso de teste, seu programa deve imprimir uma única linha contendo a expressão  
Caso NNN:, seguida dos valores do vetor resultante.

Restrições
A função de remoção deve ter complexidade O(n). 

    Entrada:    6
                1 0 2 0 3 0
                3
                0 0 0
                2
                0 1
                0
    Saída:      Caso 1: 1 2 3
                Caso 2: 
                Caso 3: 1
"""

def remove_zero(vet):
	result=[]
	for i in vet:
		if (i!=0):
			result.append(i)
	return result

count=1
n=int(input())
while(n>0):
	vet=[]
	for i in range(n):
		num=int(input())
		vet.append(num)

	vet = remove_zero(vet)
	print('Caso {}: '.format(count), end="") 
	for i in vet:
		print('{} '.format(i), end = "")
	print('')
	count+=1
	n=int(input())
