#!/usr/bin/python3

""" No universo do livro Harry Potter, o Expecto Patronum é um feitiço que cria um guardião composto de 
energia positiva, na forma de um animal prateado, único para cada bruxo. O patrono do personagem 
principal é um cervo. Escreva um programa que lê uma string representando o nome de um animal e 
verifica se esse animal é um cervo.

Entrada
A entrada conterá uma única palavra com no máximo 80 caracteres. A entrada poderá conter letras 
maiúsculas e minúsculas.

Saída
1. Se o patrono for cervo, exiba a mensagem cervo eh patrono do Harry Potter.
2. Caso contrário, exiba a mensagem <entrada> nao eh patrono do Harry Potter, 
substituindo a expressão <entrada> pela string fornecida como entrada.

	Entrada : cervo
	Saída	: cervo eh patrono do Harry Potter

	Entrada : CERVO
	Saída   : CERVO eh patrono do Harry Potter

	Entrada : asno
	Saída   : asno nao eh patrono do Harry Potter
 """
def compara_string(str1, str2):
	for i in range(len(str2)):
		aux = str2.lower()
	if(len(str1) != len(str2)):
		return 1
	for i in range(len(str2)):
		if(str1[i] != aux[i]):
			return 1
	return 0

entrada = input()
if(compara_string('cervo', entrada) == 0):
	print(entrada, 'eh patrono do Harry Potter')
else:
	print(entrada, 'nao eh patrono do Harry Potter')
