#!/usr/bin/python3

# Cálculo recursivo da função de Fibonacci
#
# Observe que essa função é extremamente complexa. A árvore de chamadas
# recursivas irá replicar as mesmas instâncias repetidamente

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

x = int(input("Digite um inteiro: "))
print("Tentando calcular o Fibonacci de", x)
fx = fib(x)
print("O Fibonacci de {0} e' {1}".format(x, fx))
