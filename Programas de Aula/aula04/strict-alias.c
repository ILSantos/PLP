#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef struct Msg
{
    unsigned int a;
    unsigned int b;
} Msg;

void SendWord(uint32_t w)
{
	printf("%u\n", (unsigned)w);
}

int main(void)
{
    // Get a 32-bit buffer from the system
    uint32_t* buff = malloc(sizeof(Msg));

    // Alias that buffer through message
    Msg* msg = (Msg*)(buff);

    // Send a bunch of messages    
    for (int i =0; i < 10; ++i)
    {
        msg->a = i;
        msg->b = i+1;
        SendWord(buff[0]);
        SendWord(buff[1]);   
    }

    return 0;
}
