###########
# gato.py 
#
# Uma classe para gatos em Python
#
# Este arquivo e' um exemplo bem simples de orientacao a objetos. Nao
# estao sendo usadas aqui as melhores praticas de desenvolvimento. O
# ideal e' declarar classes em pacotes e tomar cuidado para nao inserir
# nomes do escopo global.
#
# Para testar, voce pode executar o comando "%run gato.py" no ipython3

# Define um dicionario de cores no escopo global. Nao e' a melhor pratica.
# Se houver uma variavel com o nome "cores", ela sera' revinculada.
cores = {"branco": (255, 255, 255),
        "laranja": (223, 118,  17),
        "cinza": (160, 160, 160),
        "preto": (0, 0, 0)}


class Gato:
    """Manipula gatos.

    Atributos de classe:
      populacao (int): A quantidade de gatos no mundo.

    Atributos de instancia:
      cor (tuple): Cor do gato em RGB.
      localizacao (int): Local onde o gato se encontra.
      Humor (str): Descricao do humor do gato.

    Objetos desta classe representam gatos. A cor deve ser uma tupla de
    tres elementos indicando as componentes R, G, e B da cor do gato.
    A localizacao do gato e' um inteiro no intervalo [0, 3], indicando
    se o gato esta' no chao, sobre a mesa, sobre a pia ou em cima da
    geladeira. O humor deve ser uma string.

    A populacao e' incrementada automaticamente sempre que um novo
    objeto desta classe e' instanciado."""

    # Tamanho da populacao em numero de gatos
    populacao = 0


    def __init__(self, cor, humor):
        """Instancia um novo gato com certa cor e humor.

        A cor deve ser uma tupla de tres inteiros no intervalo [0,255]
        indicando as componentes R, G e B.

        O humor deve ser uma string.

        Inicialmente, o gato esta' sempre no chao"""

        self.cor = cor
        self.humor = humor
        self.localizacao = 0


    def altura(self):
        """Retorna a altura do gato.

        A altura do gato depende de sua localizacao:

           0 - chao
           1 - mesa
           2 - pia
           3 - geladeira"""
        return self.localizacao


    def miar(self):
        """Faz o gato miar!"""
        print("Miau!")


    def local_str(self):
        """Retorna uma string com o nome do lugar do gato."""
        lugares = ["chao", "mesa", "pia", "geladeira"]
        return lugares[self.localizacao]


    def subir(self, niveis):
        """Faz o gato subir uma quantidade de niveis.

        O parametro niveis deve ser um inteiro que indica o numero de
        niveis que o gato ira' subir. Comecando com o nivel 0, o gato
        pode subir do chao para a mesa, para a pia e finalmente para
        a geladeira.

        A geladeira e' o ultimo nivel. Se o gato tentar subir alem
        desse nivel, uma mensagem de erro sera' exibida."""
        if self.localizacao + niveis > 3:
            print("Nao e' possivel subir acima da geladeira!")
        else:
            self.localizacao += niveis


    def descer(self, niveis):
        """Faz o gato descer uma quantidade de niveis.

        O parametro niveis deve ser um inteiro que indica o numero de
        niveis que o gato ira' subir. Comecando com o nivel 3, o gato
        pode subir da geladeira para a pia, para a mesa e, finalmente,
        para o chao.

        O chao e' o ultimo nivel. Se o gato tentar descer alem desse
        nivel, uma mensagem de erro sera' exibida."""
        if self.localizacao - niveis < 0:
            print("Nao e' possivel descer abaixo do chao!")
        else:
            self.localizacao -= niveis

