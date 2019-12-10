#!/usr/bin/python

"""
Acrescente à classe Gato que você desenvolveu no exercício anterior os seguintes métodos:
    - atacar(gato:Gato) - ataca um gato causando dano igual à sua força. O método deve responder enviado ao objeto 
    gato a mensagem defender(força), sendo que o argumento força é o seu valor de força;
    - defender(int dano) - tenta se defender do ataque de outro gato. O método deve responder deduzindo de sua própria 
    energia o dano recebido, amortecido de sua defesa. A energia nunca pode ser negativa. Quando a energia chega a zero,
    o gato foge da batalha.

Por exemplo, suponha que você leu os seguintes gatos:
    "Mingau, o Barbaro", com força 110, energia 80 e defesa 90
    "Garfraco", com força 18, defesa 200 e energia 1
    "Bixena", com força 120, defesa 60 e energia 88

Podemos representar esses três gatos com os objetos:
    mingau = Gato("Mingau, o Barbaro", forca=110, energia=80, defesa=90)
    garfraco = Gato("Garfraco", forca=18, energia=1, defesa=200)
    bixena = Gato("Bixena", forca=120, defesa=60, energia=88)

Por exemplo, se quisermos que Bixena ataque Mingau, o Bárbaro, passaremos ao objeto que representa Bixena a mensagem
atacar(mingau), que por sua vez passará a mingau a mensagem defender(120). A defesa de Mingau é 90, portanto o objeto 
mingau deverá responder ao método subtraindo de sua própria energia 120−90=30 pontos.
Por outro lado, se quisermos que Bixena ataque Garfraco, passamos ao objeto que representa Bixena a mensagem 
atacar(garfraco). O gato responderá enviando ao objeto de Garfraco a mensagem defender(120). A resposta de Garfraco 
será amortizar o ataque considerando sua super-defesa (promovida por uma lasanha com dez camadas), então ele não irá 
subtrair nada de sua própria energia.
Neste exercício, você deverá ler um gato atacante e uma lista de N gatos. Em seguida, simule o ataque desse gato a 
todos os outros. Imprima mensagens indicando quanta energia sobrou em cada gato e se algum gato fugiu.


Entrada: 

A primeira linha da entrada conterá uma string codificando o gato atacante. Em seguida, haverá um inteiro N, indicando 
o número de gatos que foram atacados.

Saída:

Imprima a mensagem "{} esta atacando!"
Em seguida, imprima a energia de cada gato após os ataques, no formato "Energia de {}: {}"
Se um gato fugir, imprima também a mensagem "{} fugiu!"

    Entrada:    {"nome":"Gattacus","defesa":60,"forca":120,"energia":88}
                5
                {"nome":"Bixena","defesa":50,"forca":118,"energia":96}
                {"nome":"Mingau,_o_Barbaro","defesa":90,"forca":110,"energia":80}
                {"nome":"Tom_Matador","forca":100,"defesa":73,"energia":115}
                {"nome":"Garfraco","forca":18,"defesa":200,"energia":1}
                {"nome":"Pretinha","forca":16,"defesa":0,"energia":48}

    Saída:      Gattacus esta atacando!
                Energia de Bixena: 26
                Energia de Mingau,_o_Barbaro: 50
                Energia de Tom_Matador: 68
                Energia de Garfraco: 1
                Energia de Pretinha: 0
                Pretinha fugiu!

"""