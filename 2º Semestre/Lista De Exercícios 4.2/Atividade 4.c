/* Faça uma função que dado dois valores (X, Y) retorne X
Y, entretanto não é permitido usar a função pow da linguagem C.
Observação 1: Use a função multiplicação da questão anterior com um comando de repetição.
Observação 2: Essa questão deverá ser implementada considerando Y como do tipo int. Se Y
for float, a implementação de potência é mais complexa, pois precisaríamos trabalhar com
potência de números fracionários. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#define _USE_MATH_DEFINES 

// FUNÇÕES
float multiplicar(float x, float y)
{
    float resultado = 0;
    int vezes = (int)y;
    int negativo = 0;
    int i;

    if (vezes < 0) {
        vezes = -vezes;
        negativo = 1;
    }

    for (i = 0; i < vezes; i++) {
        resultado += x;
    }

    if (negativo) {
        resultado = -resultado;
    }

    return resultado;
}

float potencia(float base, int expoente)
{
    float resultado = 1.0;
    int exp_positivo = expoente;
    int i;

    if (exp_positivo < 0) {
        exp_positivo = -exp_positivo;
    }

    for (i = 0; i < exp_positivo; i++) {
        resultado = multiplicar(resultado, base);
    }

    if (expoente < 0) {
        return 1.0 / resultado;
    }

    return resultado;
}

// PRINCIPAL
int main()
{
    SetConsoleOutputCP(65001);

    float base, res;
    int expoente;

    printf("Digite a base (X): ");
    scanf("%f", &base);

    printf("Digite o expoente inteiro (Y): ");
    scanf("%d", &expoente);

    res = potencia(base, expoente);

    printf("\nResultado de %.2f ^ %d = %.4f\n", base, expoente, res);

    return 0;
}