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

def strequal(string1,string2):
	for i in range (len(string2)):
		aux = string2.lower()
	
	if(len(string1)!=len(string2)):
		return 1;
	
	for i in range (len(string1)):
		if(string1[i] != aux[i]):
			return 1;
	return 0
	
entrada = input()

if (strequal("cervo",entrada)==0):
	print(entrada,"eh patrono do Harry Potter")
else:
	print(entrada,"nao eh patrono do Harry Potter")
