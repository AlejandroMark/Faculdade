/* Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte
a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um
fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante
perderá. Exiba o total de dias.  */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main()
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int cigarrosPorDia, anos;
    int totalMinutos, totalDias;

    printf("Digite a quantidade de cigarros fumados por dia: ");
    scanf("%d", &cigarrosPorDia);

    printf("Digite quantos anos a pessoa fuma: ");
    scanf("%d", &anos);

    totalMinutos = cigarrosPorDia * 10 * (anos * 365);

    totalDias = totalMinutos / (24 * 60);

    printf("\nTotal de dias de vida perdidos: %d dias\n", totalDias);

    return 0;
}