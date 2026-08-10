/* Faça agora o contrário, de Fahrenheit para Celsius.  */
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() {

    // Para acentuação
    SetConsoleOutputCP(65001);
    float F, C;

    printf("Digite a temperatura em Fahrenheit: ");
    scanf("%f", &F);

    C = 5 * (F - 32) / 9;

    printf("Temperatura em Celsius: %.2f C\n", C);

    return 0;
}