#!/usr/bin/python3 
""" 
Um simples algoritmo para calcular uma potência com expoente inteiro consiste em fazer várias repetidas. 
Esse algoritmo possui complexidade O(n), pois o número de operações será uma função linear ao tamanho da
entrada. Por exemplo, para calcular 2^520 precisaremos multiplicar o número 2 520 vezes.

Existem diversos algoritmos que permitem reduzir essa complexidade. Um simples algoritmo de divisão e conquista
tem como base os fatos de que x^2n = (x^n)^2 e que x^2n+1 = x . x^2n. Essa simples relação permite reduzir pela metade
o número de passos para calcular x^2n.

Por exemplo, para calcular 2^27, precisamos fazer apenas 7 multiplicações, em vez de 27:
2^27 = 2 x 2^26
           2^26 = 2^13 x 2^13
                  2^13 = 2 x 2^12
                  .
                  .
                  .
Neste exercício você deverá implementar uma função denominada f(b, e) que usa a seguinte relação de recorrência para 
encontrar a potência b^e:

b^e = b x b^e-1, se e é impar | b^e/2 x b^e/3 , se e é par

Assuma que tanto b quanto e serão valores inteiros e que e >= 0. Não se esqueça de definir os casos base da recursão.

Entrada
A entrada conterá vários pares de linhas contendo os inteiros b e e.

A sáida termina quando e < 0. Esse caso é um sentinela e não deve ser processado.

Saída
Para cada par lido, imprima em uma única linha o resultado da potenciação b^e.

    Entrada:    10 2
                2 10
                5 0
                0 -1
    Saída:      100
                1024
                1        
"""
def lePares():
	while True:
		b = int(input())
		e = int(input())
		if e < 0: return
		yield (b, e)

def pot(b, e):
	pass
		
for (b, e) in lePares():
	print(pot(b, e))