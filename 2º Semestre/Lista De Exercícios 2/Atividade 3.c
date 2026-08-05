/* Dados três valores A, B e C, construa um programa em C que imprima os valores de forma
decrescente (do maior para o menor). */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float A, B, C;

    printf("Informe O Valor A: ");
    scanf("%f", &A);

    printf("Informe O Valor B: ");
    scanf("%f", &B);

    printf("Informe O Valor C: ");
    scanf("%f", &C);

    printf("\nValores em ordem decrescente:\n");

    if (A >= B && B >= C) {
        printf("%.2f, %.2f, %.2f\n", A, B, C);
    } 
    else if (A >= C && C >= B) {
        printf("%.2f, %.2f, %.2f\n", A, C, B);
    } 
    else if (B >= A && A >= C) {
        printf("%.2f, %.2f, %.2f\n", B, A, C);
    } 
    else if (B >= C && C >= A) {
        printf("%.2f, %.2f, %.2f\n", B, C, A);
    } 
    else if (C >= A && A >= B) {
        printf("%.2f, %.2f, %.2f\n", C, A, B);
    } 
    else {
        printf("%.2f, %.2f, %.2f\n", C, B, A);
    }

    return 0;
}