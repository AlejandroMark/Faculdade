/* Desenvolva um programa em C que leia uma temperatura em graus centígrados e
apresente a temperatura convertida em graus Fahrenheit. A fórmula de conversão é:
F = (9 x C + 160) / 5
Onde F é a temperatura em Fahrenheit e C é a temperatura em centígrados */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() {
    float C, F;

    printf("Digite a temperatura em graus Celsius: ");
    scanf("%f", &C);

    F = (9 * C + 160) / 5;

    printf("Temperatura em Fahrenheit: %.2f F\n", F);

    return 0;
}
