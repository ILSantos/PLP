#include <stdio.h>
#include <limits.h>

int main(void)
{
	printf("Bits por byte: %d\n", CHAR_BIT);
	printf("sizeof (char): 1 byte (%d bits)\n", CHAR_BIT);
	printf("sizeof (int) : %d bytes (%d bits)\n", 
			sizeof (int), sizeof (int) * CHAR_BIT);
	printf("Intervalo do (char): [%d, %d]\n", CHAR_MIN, CHAR_MAX);
	printf("Intervalo do (int) : [%d, %d]\n", INT_MIN, INT_MAX);
	return 0;
}
