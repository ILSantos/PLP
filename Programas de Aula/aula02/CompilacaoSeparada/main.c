/* Programa "principal".
 *
 * Para efetuar a compilacao seaprada com o GCC:
 *
 * gcc main.c -c
 * gcc hello.c -c
 * gcc main.o hello.o
 * ./a.out
 */

/* Prototipo da funcao hello(). Normalmente estaria em um
 * arquivo .h
 */

void hello(void);

int main(void)
{
    hello();
    return 0;
}
