def le_pares():
    while True:
        a = int(input())
        b = int(input())
        if b < 0: return
        yield (a, b)

for p in le_pares():
    print("par =", p)
