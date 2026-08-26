/* Criar um programa em C que receba o valor de x, e calcule e imprima o valor de f(x).
f(x) = {
  1,    se x ≤ 1
  2,    se 1 < x ≤ 2
  x²,   se 2 < x ≤ 3
  x³,   se x > 3
} */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

int main() 
{
    SetConsoleOutputCP(65001);

    float x, fx;

    printf("Digite o valor de x: ");
    scanf("%f", &x);

    if (x <= 1) {
        fx = 1;
    } 
    else if (x <= 2) {
        fx = 2;
    } 
    else if (x <= 3) {
        fx = pow(x, 2);
    } 
    else {
        fx = pow(x, 3);
    }

    printf("\nf(%.2f) = %.2f\n", x, fx);

    return 0;
}