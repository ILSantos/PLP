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
