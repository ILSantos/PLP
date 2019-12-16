#include <iostream>
#include <string>

using std::cout;
using std::string;

class Pessoa {
  /* A classe Pessoa representa pessoas genéricas. Toda pessoa possui
   * um nome. O nome é um atributo protegido para que possa ser
   * acessado por classes derivadas, mas não é público porque a
   * pessoa sabe seu nome. Outros objetos perguntam.
   */
protected:  
  string nome;

public:
  /* O construtor da classe define o nome da pessoa no seu nascimento.
   */
  Pessoa(const char *nome) {
    this->nome = string(nome);
  }

  /* Quando a pessoa fala, ela se apresenta como uma pessoa.
   */
  void falar() {
    cout << "Sou uma pessoa e meu nome é " << nome << "\n";
  }
};



class Professor : public Pessoa {
public:
  /* A classe Professor estende a classe Pessoa. Professores são
   * pessoas com especialização de profissisão. Mas o construtor de
   * Professor é igual ao de Pessoa. Tudo o o que ele faz é ativar o
   * construtor de Pessoa. Ambos têm o mesmo estado inicial.
   */
  Professor(const char *nome)
    : Pessoa(nome)
    { }

  /* A fala do professor é igual à de Pessoa. Mas ele se apresenta
   * como um professor.
   */
  void falar() {
    cout << "Sou um professor e meu nome é " << nome << "\n";
  }
};


void apresentar(Pessoa *a, Pessoa *b);

int main()
{
  Professor *girafales = new Professor("Inocêncio");
  Pessoa *chiquinha = new Pessoa("Chiquinha");

  apresentar(girafales, chiquinha);
}


/* Diferentemente do que vimos em Java, as classes "Pessoa" e
 * "Professor", da forma como implementamos, não obedece o princípío
 * de substituição de Leskov.
 *
 * Quando a mensagem "fala" é passada para os dois objetos "a" e "b",
 * o despacho é feito para a classe "Pessoa", pois as mensagens
 * estão vinculadas com o método da classe, não com o objeto.
 *
 * Para que esse exemplo siga corretamente o princípio de
 * substituição de Leskov, é necessário declarar o método falar como
 * "virtual".
 */
void apresentar(Pessoa *a, Pessoa *b)
{
  cout << "Duas pessoas se encontram pela primeira vez\n";
  cout << "A primeira diz:\n- ";
  a->falar();
  cout << "A segunda responde:\n- ";
  b->falar();
}

