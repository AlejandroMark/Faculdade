/* Seja a seguinte série:
1, 4, 9, 16, 25, 36, ...
Implemente um programa que gere esta série até o N-ésimo (último) termo. Este N-ésimo
termo é digitado pelo usuário. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int n, i;

    do {
        printf("Informe o valor de N (quantidade de termos): ");
        scanf("%d", &n);

        if (n <= 0) {
            printf("Quantidade inválida! Digite um valor maior que 0.\n\n");
        }
    } while (n <= 0);

    printf("\nSérie até o %dº termo:\n", n);

    for (i = 1; i <= n; i++) 
    {
        printf("%d ", i * i);
    }

    printf("\n");

    return 0;
}