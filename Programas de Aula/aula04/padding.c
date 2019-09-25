#include <stdio.h>

struct {
    char c;
    int d;
} estrutura;

int main(void)
{
    printf("sizeof (char): %d\n", sizeof (char));
    printf("sizeof (int) : %d\n", sizeof (int));
    printf("sizeof estrutura: %d\n", sizeof estrutura);
}
