/* Implemente um programa em C que leia um número e imprima a raiz quadrada deste
número caso ele seja positivo ou igual a zero; e o quadrado do número caso ele seja
negativo. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float num;
    printf("Informe Um Número: ");
    scanf("%f", &num);


    if (num >= 0) {
        printf("A Raiz Quadrada Do Número É De: %.2f\n", sqrt(num));
    }
    else {
        printf("O Quadrado Do Número É De: %.2f\n", pow(num, 2));
    }

    return 0;
}