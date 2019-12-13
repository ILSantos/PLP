#!/usr/bin/python3

class Pessoa:
  """A classe Pessoa representa pessoas genéricas.

  Toda pessoa possui um nome. Declaramos um atributo privado, pois
  em tese, outras pessoas não têm acesso direto aos nossos nomes.
  Elas têm que nos perguntar."""
 
  def __init__(self, nome):
    """Construtor da classe. Define o nome da instância."""
    self._nome = nome

  def falar(self):
    """Fala com outras pessoas e se apresenta pelo nome."""
    print("Sou uma pessoa e meu nome é " + self._nome)



class Professor(Pessoa):
  """A classe Professor estende a classe Pessoa.

  Professores são pessoas com especialização de profissisão."""

  # Não é necessário construtor. A classe Professor herda o
  # construtor de Pessoa com os mesmos argumentos

  def falar(self):
    """Fala com outras pessoas e se apresenta como professor."""
    print("Sou um professor e meu nome é " + self._nome)


def apresentar(a, b):
    # O polimorfismo de herança funciona em Python, mas por causa
    # duck typing. Objetos da classe Professor herdam todos os
    # métodos de Pessoa e os vínculos são sempre dinâmicos
    print("Duas pessoas se encontram pela primeira vez.");
    print("A primeira diz:\n- ", end='')
    a.falar();
    print("A segunda responde:\n- ", end='');
    b.falar();


girafales = Professor('Inocêncio')
chiquinha = Pessoa('Chiquinha')
apresentar(girafales, chiquinha)
