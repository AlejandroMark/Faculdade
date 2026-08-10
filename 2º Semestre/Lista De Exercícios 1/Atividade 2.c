/* Uma P.G. (progressão geométrica) fica determinada pela sua razão (q) e pelo primeiro
termo (a1). Implemente um programa em C que seja capaz de determinar qualquer
termo de uma P.G., dado a razão e o primeiro termo.
an = a1 x q(n - 1) */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float a1, q, n, an;

    printf("Digite o primeiro termo (a1): ");
    scanf("%f", &a1);

    printf("Digite a razão (q): ");
    scanf("%f", &q);

    printf("Digite a posição do termo desejado (n): ");
    scanf("%f", &n);

    an = (a1 * q) * (n - 1); 

    printf("\nO termo desejado da P.G. é: %.2f\n", an);

    return 0;
}