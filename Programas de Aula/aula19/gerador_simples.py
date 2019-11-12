# Um gerador que produz a sequência (1, 2, 3)
def gerador_simples():
    yield 1
    yield 2
    yield 3

# Um laço para consumir a sequência
for i in gerador_simples():
    print(i)
