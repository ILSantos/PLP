#!/usr/bin/python3 

""" 
Implemente um programa que faça a multiplicação matricial de duas matrizes, MatA e MatB, lidas via teclado. 
Considere no algoritmo que só podemos multiplicar matrizes de ordem compatíveis. Não use o módulo Numpy.

Entrada
A entrada conterá vários casos de teste. Inicialmente, haverá dois inteiros LA e CA indicando, respectivamente, 
o número de linhas e de colunas da matriz A. Os LA×CA valores seguintes serão números em ponto flutuante contendo 
os elementos da matriz A.Em seguida, haverá dois inteiros LB e CB indicando, respectivamente, o número de linhas e 
de colunas da matriz , seguidos de LB×CB números em ponto flutuante.Em todos os casos, nenuma dimensão (linhas e
colunas) será menor que 1 ou maior que 10.
A entrada termina com um caso sentinela no qual LA=CA=0. Esse caso não deve ser processado.

Saída
Para cada caso de entrada, imprima primeiramente o texto 'Caso #%d 'em uma única linha. Em seguida, imprima, com 
duas casas de precisão, os valores da matriz resultante A×B.

    Entrada:    3 2

                1 2
                3 4
                5 6

                2 3

                1 2 3
                4 5 6

                2 2

                1 0
                0 1

                2 2

                2 2
                2 2

                0 0
    Saída:      'Caso #1'
                9.00 12.00 15.00
                19.00 26.00 33.00
                29.00 40.00 51.00
                'Caso #2'
                2.00 2.00
                2.00 2.00
"""

def matmul(m,n,p,matriz1,matriz2,result):
	for i in range(m):
		linha=[]
		for j in range(p):
			linha.append(0)
		result.append(linha)
		
	for i in range(m):
		for j in range(p):
			for k in range(n):
				result[i][j] = result[i][j] + (matriz1[i][k] * matriz2[k][j])
			

m = int(input())
n1 = int(input())
cont = 1
while(m!=0 and n1!=0):
	matriz1 = []
	for i in range(m):
		linha = []
		for j in range(n1):
			num = float(input())
			linha.append(num)
		matriz1.append(linha)
		
	n2 = int(input())
	p = int(input())

	matriz2 = []
	for i in range(n2):
		linha = []
		for j in range(p):
			num = float(input())
			linha.append(num)
		matriz2.append(linha)
	result=[]	
	if(n1==n2):
		matmul(m,n1,p,matriz1,matriz2,result)
		print('Caso #{} '.format(cont), end="\n") 
		for i in range (m):
			string = ""
			for j in result[i]:
				string = string + "{:.2f} ".format(j)
			print(string)
			
	else:
		print('Caso #{} '.format(cont), end="") 
	cont+=1
		
	m = int(input())
	n1 = int(input())
