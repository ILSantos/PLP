class Pessoa {
  /* A classe Pessoa representa pessoas genéricas. Toda pessoa possui
   * um nome. O nome é um atributo protegido para que possa ser
   * acessado por classes derivadas, mas não é público porque a
   * pessoa sabe seu nome. Outros objetos perguntam.
   */
  protected String nome;

  /* O construtor da classe define o nome da pessoa no seu nascimento.
   */
  public Pessoa(String nome) {
    this.nome = nome;
  }

  /* Quando a pessoa fala, ela se apresenta como uma pessoa.
   */
  public void falar() {
    System.out.println("Sou uma pessoa e meu nome é " + nome);
  }
}



class Professor extends Pessoa {
  /* A classe Professor estende a classe Pessoa. Professores são
   * pessoas com especialização de profissisão. Mas o construtor de
   * Professor é igual ao de Pessoa. Tudo o o que ele faz é ativar o
   * construtor de Pessoa. Ambos têm o mesmo estado inicial.
   */
  public Professor(String nome) {
    super(nome);
  }

  /* A fala do professor é igual à de Pessoa. Mas ele se apresenta
   * como um professor.
   */
  public void falar() {
    System.out.println("Sou um professor e meu nome é " + nome);
  }
}



public class isa {
  /* A classe isa apenas implementa o programa principal
   */

  /* O método "apresentar" serve para apresentar duas pessoas que se
   * encontram pela primeira vez.
   */
  public static void apresentar(Pessoa a, Pessoa b) {
    System.out.println("Duas pessoas se encontram pela primeira vez.");
    System.out.print("A primeira diz:\n- ");
    a.falar();
    System.out.print("A segunda responde:\n- ");
    b.falar();
  }

  /* Demonstração do princípio de substituição de Leskov. Temos um
   * objeto da classe Professor e um objeto da classe Pessoa. Mas
   * objetos Professor também são objetos Pessoa. Portanto os dois
   * podem ser passados para o método apresentar(Pessoa, Pessoa)
   */
  public static void main(String args[]) {
    Professor girafales = new Professor("Inocêncio");
    Pessoa chiquinha = new Pessoa("Chiquinha");

    apresentar(girafales, chiquinha);
  }
}
