#include <iostream>

// Se removermos o comentario da linha abaixo, teremos um conflito
// de nomes. O objeto "cout" e a funcao "cout()" estarao no mesmo
// escopo. Normalmente o comando "using namespace std" eh uma ma
// pratica de programacao. Ele definitivamente nao deve ser
// utilizado em arquivos .h
//using namespace std;

// Aqui declaramos uma funcao chamada cout. Esta funcao nao tem
// nenhum proposito especifico, exceto demonstrar os espacos de
// nomes.
void cout()
{
	// Utiliza o objeto "cout" da biblioteca padrao, definido
	// no espaco de nomes "std".
	std::cout << "Nao ha conflito de nomes.\n";
}

int main()
{
	// Chama a funcao "cout()" declarada neste arquivo.
	cout();
}
