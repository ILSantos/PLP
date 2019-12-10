#!/usr/bin/python

"""
 Defina uma classe para representar gatos. Essa classe deve conter os seguintes atributos de instância:
	nome:str - o nome do gato
	energia:int - um inteiro que representa a quantidade de "energia interna" que o gato contém
	defesa:int - um inteiro que representa a proteção que o gato tem (pelagem, armadura, lasanhas etc.)
	forca:int - um inteiro que representa a quantidade de "força" do gato

A classe não deve conter atributos de classe.

A classe deve conter apenas o construtor, cujo propósito é apenas iniciar o objeto em um estado bem definido.

Em seguida, leia um programa que lê vários dicionários que representam os atributos de um gato. Instancie os gatos e imprima o nome do gato mais 
forte e o nome do gato mais fraco.

Entrada: 
O primeiro  valor da entrada será um inteiro N, indicando o número de dicionários no gatil. As N linhas seguintes serão dicionários. Leia cada linha
com sys.stdin e use eval() para converter a string lida em um objeto Python

Saída:
Imprima a saída de acordo com os casos de exemplo.


	Entrada: 6
		{"nome":"Gattacus","defesa":60,"forca":120,"energia":88}
		{"nome":"Bixena","defesa":50,"forca":118,"energia":96}
		{"nome":"Mingau,_o_Barbaro","defesa":90,"forca":110,"energia":80}
		{"nome":"Tom_Matador","forca":100,"defesa":73,"energia":115}
		{"nome":"Garfraco","forca":18,"defesa":200,"energia":1}
		{"nome":"Pretinha","forca":16,"defesa":0,"energia":48}

	Saida: 	O gato mais fraco eh Pretinha, com forca 16
		O gato mais forte eh Gattacus, com forca 120
"""
class Gato:
	def __init__(self, nome, forca, defesa, energia):
		self.nome = nome
		self.energia = energia
		self.defesa = defesa
		self.forca = forca

