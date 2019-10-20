/* Este programa tem uma árvore sintática abstrata semelhante à do programa "badc.c"
 *
 * Porém, diferentemente do outro caso, o operador de conjunção (&&) especifica que o operando
 * à esquerda é avaliado primeiro. Isso é necessário para permitir que haja avaliação de
 * curto-circuito.
 *
 * Este programa imprimirá primeiramente "Hello", depois " " e, finalmente, "world!"
 */

#include <stdio.h>

int main(void)
{
    int x = printf("Hello") && printf(" ")
        && printf("world!\n");
    printf("%d\n", x);
    return 0;
}
