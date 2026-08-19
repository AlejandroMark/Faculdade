/* Criar um programa que leia os limites inferior e superior de um intervalo e imprima todos os
números pares no intervalo aberto e seu somatório. Suponha que os dados digitados são para
um intervalo crescente, ou seja, o primeiro valor é menor que o segundo (coloque a validação
para isso). */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int lim_inf, lim_sup, i;
    int soma = 0;

    do {
        printf("Informe o limite inferior do intervalo: ");
        scanf("%d", &lim_inf);

        printf("Informe o limite superior do intervalo: ");
        scanf("%d", &lim_sup);

        if (lim_inf >= lim_sup) {
            printf("\nIntervalo inválido! O limite inferior deve ser MENOR que o limite superior.\n\n");
        }
    } while (lim_inf >= lim_sup);

    printf("\nNúmeros pares no intervalo aberto (%d, %d):\n", lim_inf, lim_sup);

    for (i = lim_inf + 1; i < lim_sup; i++) 
    {
        if (i % 2 == 0) {
            printf("%d ", i);
            soma = soma + i;
        }
    }

    printf("\n\nSomatório dos números pares: %d\n", soma);

    return 0;
}