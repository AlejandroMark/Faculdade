/* Criar um programa em Linguagem C que leia dois valores para as variáveis A e B, que
efetue a troca dos valores de forma que a variável A passe a ter o valor da variável B e que
a variável B passe a ter o valor da variável A. Apresente os valores trocados. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main()
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int A, B, aux;

    printf("Digite o valor de A: ");
    scanf("%d", &A);

    printf("Digite o valor de B: ");
    scanf("%d", &B);

    aux = A;
    A = B;
    B = aux;

    printf("\nValores trocados:\n");
    printf("A = %d\n", A);
    printf("B = %d\n", B);

    return 0;
}