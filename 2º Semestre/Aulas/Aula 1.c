#include <stdio.h>
#include <stdlib.h>

void main()
{
    int numero, matricula;
    float saldo;
    char sexo;

    //printf("Hello World!\n");

    //numero = 10;
    //matricula = 123;
    //saldo = 1000.54;

    printf("Digite Um Numero: ");
    scanf("%d", &numero);

    printf("Digite Sua Matricula: ");
    scanf("%d", &matricula);

    printf("Digite O Saldo: ");
    scanf("%f", &saldo);

    printf("Sexo: ");
    scanf(" %c", &sexo);

    printf("Numero: %d - Matricula: %d - Saldo: %.2f - Sexo: %c", numero, matricula, saldo, sexo);

    return 0;
}