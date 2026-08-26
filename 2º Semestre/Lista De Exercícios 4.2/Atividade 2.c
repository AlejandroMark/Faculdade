/* Sabendo-se que um triângulo é formado por três pontos:
A = ( X1, Y1 ) B = ( X2, Y2 ) C = ( X3, Y3 )
E que o perímetro de um triângulo é a soma das distâncias dos lados do triângulo. Podendo ser
escrito da seguinte forma:
Perímetro = DISTANCIA(A,B) + DISTANCIA(A,C) + DISTANCIA(B,C)
Faça uma função que calcule o perímetro de um triângulo.
Observação 1: Use a função distância e a função da leitura dos pontos da questão anterior. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#define _USE_MATH_DEFINES 

// FUNÇÕES
void lerPonto(float *x, float *y){

    printf("Ponto 1: ");
    scanf("%f", x);
    printf("Ponto 2: ");
    scanf("%f", y);
}

float calcularDistancia(float x1, float y1, float x2, float y2){

    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

float calcularPerimetro(float x1, float y1, float x2, float y2, float x3, float y3){

    float dAB = calcularDistancia(x1, y1, x2, y2);
    float dAC = calcularDistancia(x1, y1, x3, y3);
    float dBC = calcularDistancia(x2, y2, x3, y3);

    return dAB + dAC + dBC;
}

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float x1, y1;
    float x2, y2;
    float x3, y3;
    float perimetro;

    printf("Ponto A\n");
    lerPonto(&x1, &y1);

    printf("Ponto B\n");
    lerPonto(&x2, &y2);

    printf("\n Ponto C\n");
    lerPonto(&x3, &y3);

    perimetro = calcularPerimetro(x1, y1, x2, y2, x3, y3);

    printf("\nPerímetro do triângulo: %.2f\n", perimetro);

    return 0;
}