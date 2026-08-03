/* Uma P.A. (progressão aritmética) fica determinada pela sua razão (r) e pelo primeiro
termo(a1). Faça um programa em linguagem C, que seja capaz de determinar qualquer
termo de uma P.A., dada a razão, o primeiro termo e a quantidade de termos.
an = a1 + (n-1) x r */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void main()
{
    SetConsoleOutputCP(65001);

    float a1, n, r, an;

    printf("Digite o A1: ");
    scanf("%f", &a1);

    printf("Digite o N: ");
    scanf("%f", &n);

    printf("Digite o R: ");
    scanf("%f", &r);

    an = a1 + (n - 1) * r;

    printf("O Termo an É: %.2f\n", an);

    return 0;
}