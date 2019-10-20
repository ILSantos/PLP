/* Exemplo de comportamento indefinido em C
 *
 * A árvore sintática abstrata do programa é:
 *
 *
 *                                            + (operação soma)
 *                         .---------------------------------.
 *                         |                                 |
 *                         + (operação soma)         printf("world!\n");
 *           .---------------------.
 *          |                      |
 *    printf("Hello")        printf(" ")
 *
 *
 * Sintaticamente, o programa é válido. Ele realiza a soma de três expressões (chamadas de
 * funções). Entretanto, a semântica desse programa é indefinida, pois a linguagem não
 * especifica em qual ordem os operandos (isto é, as chamadas) devem ser avaliados.
 *
 * Dependendo da ordem escolhida pelo compilador, a chamada printf("Hello") pode ser
 * executada antes ou depois da chamada de printf("world!\n").
 *
 * Programas cujo resultado dependem da ordem de avaliação dos operandos têm comportamento
 * indefinido (semântica indefinida).
 */

#include <stdio.h>

int main(void)
{
    int x = printf("Hello") + printf(" ") + printf("world!\n");
    printf("%d\n", x);
    return 0;
}
