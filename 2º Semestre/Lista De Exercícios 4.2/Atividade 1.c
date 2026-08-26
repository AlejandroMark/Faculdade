/* Escreva uma função que calcule a distância entre dois pontos, sabendo que a
distância entre dois pontos é dada pela expressão:
DISTANCIA = ( ( X2 – X1 )2 + ( Y2 – Y1 )2)1/2
O primeiro ponto é (X1, Y1) e o segundo ponto é dado por (X2, Y2).
Observação 1: Crie apenas uma função para a leitura dos pontos (X,Y), com passagem de
parâmetros por referência. Chame essa função duas vezes, uma para cada ponto.
Observação 2: Para essa questão poderão ser utilizadas as funções pow e/ou sqrt da
biblioteca <math.h> da linguagem C. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#define _USE_MATH_DEFINES 

// FUNÇÕES
void lerPonto(float *x, float *y){
    printf("Valor X: ");
    scanf("%f", x);
    printf("Valor Y: ");
    scanf("%f", y);
}

float calcularDistancia(float x1, float y1, float x2, float y2){
    float dist;
    dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    return dist;
} 

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float x1, y1, x2, y2;
    float distancia;

    printf("Ponto 1 ");
    lerPonto(&x1, &y1);

    printf("Ponto 2 ");
    lerPonto(&x2, &y2);

    distancia = calcularDistancia(x1, y1, x2, y2);

    printf("Distancia Entre Os Pontos: %.2f", distancia);

    return 0;
}