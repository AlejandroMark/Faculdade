#include <stdio.h>
#include <stdlib.h>

int main() 
{
    float varInt;
    float varReal;
    int porc;

    printf("Digite: ");
    scanf("%d", &porc);

    // Divisão entre números INTEIROS e resultado é INTEIRO
    varInt = 190.0/100;
    varReal = (float) porc / 100;
    
    printf ("Inteiro: %f\n", varInt);
    printf ("Real: %f\n", varReal);

    return 0;
}