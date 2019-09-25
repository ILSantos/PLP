#include <stdio.h>

// A inclusao do arquivo .h nao eh necessaria neste exemplo, mas normalmente
// os "modulos" incluem seus proprios arquivos ".h"
//
// Isso garante que as funcoes declaradas no arquivo ".c" terao os mesmos
// cabecalhos que aquelas do arquivo ".h" e tambem remove dependencia de
// ordem entre as declaracoes no arquivo ".c"
#include "hello.h"

void hello(void)
{
    printf("Hello, world!\n");
}
