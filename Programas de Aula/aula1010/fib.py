def fib(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

x = int(input("Digite um inteiro: "))
fx = fib(x)
print("O fibonacci de {0} e' {1}".format(x, fx))