#!/usr/bin/python3 

""" Escreva uma função para realizar busca binária em um vetor de inteiros ordenado. Em seguida, escreva uma função f(L, x)
que verifica se a lista L contém dois elementos distintos cuja soma seja exatamente x. Por exemplo, se L=(1,3,4,6,9) e 
x=10, então a função deve retornar um valor verdadeiro, pois 1+9=10. Além disso, 4+6=10, mas apenas um par de elementos 
seria suficiente. Por outro lado, se x=8, então a função deve retornar um valor falso, pois não existem dois elementos 
distintos em L cuja soma seja 8.

Entrada
A entrada conterá apenas um caso de teste. O primeiro elemento da entrada será um inteiro N indicando o tamanho da lista. 
Em seguida, haverá N inteiros. Após a lista, haverá um inteiro Q indicando o número de consultas. Os Q inteiros seguintes 
serão as consultas x1, x2, ldots, xQ.

Saída
Para cada consulta, você deve verificar se existm dois elementos distintos na lista cuja soma seja xi. Imprima em uma única 
linha a palavra sim ou a palavra nao.

Restrições
Utilize a sua própria função de busca binária para obter uma complexidade de O(n⋅logn). Isto é, faça o mínimo necessário de 
comparações. Não compare todos os pares de elementos para verificar a soma.

    Entrada:    5
                -1 1 1 5 8
                3
                2 7 0
    Saída:      sim
                nao
                sim 
"""
def binario(list, dif):
	inicio = 0
	fim = len(list)-1
	while(inicio < fim):
		meio = int((inicio + fim) / 2)
		if(list[meio] == dif):
			return meio
		elif(dif < list[meio]):
			fim = meio - 1
		else:
			inicio = meio + 1
	return -1

def f(list, x):
	for i in list:
		dif = x - i
		resultado = binario(list, dif)
		if(resultado != - 1):
			return True
	return False

n = int(input())
vetor = []
consulta = []
for i in range(n):
	num = int(input())
	vetor.append(num)

q = int(input())
for i in range(q):
	num = int(input())
	consulta.append(num)

for i in consulta:
	if (f(vetor,i) == True):
		print("sim")
	else:
		print("nao")
