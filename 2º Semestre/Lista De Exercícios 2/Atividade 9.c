/* Construir um programa em C para calcular as raízes de uma equação do 2º grau, sendo
que os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário através do
teclado. Calcular e exibir as raízes da equação e dizer se a concavidade da parábola
correspondente é voltada para cima ou para baixo.
Delta:
Delta Raízes
Delta < 0 Não há solução real
Delta = 0 Há duas soluções reais iguais
Delta > 0 Há duas soluções reais diferentes
Concavidade:
 Valor de a Concavidade
a > 0 Concavidade voltada para cima
a = 0 Não é uma equação de 2° grau
a < 0 Concavidade voltada para baixo
Exemplo:
 Equação: 2x2 + 7x + 5 = 0
 Coeficientes: a = 2; b = 7; c = 5
 Raízes: x1 = -1 e x2 = -2,5
 Concavidade voltada para cima  */

 #include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

int main() 
{
    SetConsoleOutputCP(65001);

    float a, b, c;
    float delta, x1, x2;

    printf("Digite o coeficiente A: ");
    scanf("%f", &a);

    printf("Digite o coeficiente B: ");
    scanf("%f", &b);

    printf("Digite o coeficiente C: ");
    scanf("%f", &c);

    // Verifica se é uma equação do 2º grau
    if (a == 0) {
        printf("\nNão é uma equação de 2° grau (A deve ser diferente de 0).\n");
    } 
    else {
        delta = pow(b, 2) - 4 * a * c;

        printf("\n--- Resultados ---\n");
        printf("Delta = %.2f\n", delta);

        // Raízes
        if (delta < 0) {
            printf("Não há solução real.\n");
        } 
        else if (delta == 0) {
            x1 = -b / (2 * a);
            printf("Há duas soluções reais iguais: x1 = x2 = %.2f\n", x1);
        } 
        else {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);
            printf("Há duas soluções reais diferentes: x1 = %.2f e x2 = %.2f\n", x1, x2);
        }

        // Concavidade
        if (a > 0) {
            printf("Concavidade voltada para cima\n");
        } 
        else {
            printf("Concavidade voltada para baixo\n");
        }
    }

    return 0;
}