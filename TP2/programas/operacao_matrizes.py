#!/usr/bin/python3

def determinante(matriz):
    n = len(matriz)
    aux = [0] * n
    total = 1
    det = 1

    #loop de iteração pelos elementos diagonais
    for i in range(0,n):
        index = i
	#pega os valores da coluna exterior procurando por uma que o valor 		não é zero
        while index < n and matriz[index][i]  == 0:
            index += 1
        if index == n: #se não encontrar nenhum valor diferente de zero interrompe o laço e recomeça um novo laço no for
            continue
        if index != i:
	    #troca de lugar o index e o valor da linha
            for j in range(0,n):
                matriz[index][j], matriz[i][j] = matriz[i][j], matriz[index][j]
	    #troca o sinal do determinante ao trocar de linha
            det = det * int(pow(-1, index-i))
	#guarda os valores da diagonal
        for j in range(0, n):
            aux[j] = matriz[i][j]
	#faz a transversal dos valores embaixo da matriz principal
        for j in range(i+1, n):
            n1 = aux[i] 	# valor da matriz principal
            n2 = matriz[j][i]	# valor da linha nao principal
	    # fa a transversal das outras linhas e multiplica as linhas
            for k in range(0, n):
                matriz[j][k] = (n1 * matriz[j][k]) - (n2 * aux[k])
            total = total * n1 	#det(kA) = kDet(A)
    #multiplica a transversal pra obter o determinante
    for i in range(0, n):
        det = det * matriz[i][i]
    return int(det / total)	#det(kA)/ k=Det(A)

def transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def cofator(matriz, a, b):
    n = len(matriz)
    m = [[matriz[i][j] for j in range(n) if j != b] for i in range(n) if i != a]
    return determinante(m) * (-1)**(a+b)

def matriz_cofatores(matriz):
    n = len(matriz)
    return [[cofator(matriz, i, j) for j in range(n)] for i in range(n)]

def inversa(matriz):
    n = len(matriz)
    det = determinante([matriz[i][:] for i in range(n)])
    if det == 0:
        raise ZeroDivisionError("Matriz nao tem inversa")
    adjunta = transposta(matriz_cofatores(matriz))
    return [[(1./det) * adjunta[i][j] for j in range(n)] for i in range(n)]

