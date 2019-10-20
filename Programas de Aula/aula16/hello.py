#!/usr/bin/python3

def saystr(str_):
    # Uma função que imprime o parâmetro
    # O método "format" faz interpolação das chaves na string e as
    # substitui pelo valor da variável
    print("I say '{}'".format(str_))

# Usa a função com uma variável do tipo string
x = "hello"
saystr(x)

# Usa a função com uma variável do tipo int (exemplo de duck typing)
saystr(42)
