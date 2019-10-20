#!/usr/bin/python3

# Exemplo de manipulação de listas
#
# Declara uma lista vazia e preenche com os valores de Fibonacci para 0, 1, 2, 3, ..., n

def fib(n):
    l = []

    # A função len() retorna o número de elementos em uma lista
    while len(l) <= n:
        if (len(l) == 0) or (len(l) == 1):
            # A função append() adiciona um elemento ao fim da lista
            l.append(1)
        else:
            # A notação -1 é utilizada para acessar o último elemento da lista
            ultimo = l[-1]
            penultimo = l[-2]
            l.append(ultimo + penultimo)

    return l


