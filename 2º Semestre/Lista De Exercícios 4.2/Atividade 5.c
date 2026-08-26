/* Implemente um algoritmo de calculadora que faça as operações de:
- Adição
- Subtração
- Divisão
- Multiplicação (usando a função da questão 3)
- Potência (usando a função da questão 4) */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#define _USE_MATH_DEFINES 

// FUNÇÕES
float somar(float a, float b)
{
    return a + b;
}

float subtrair(float a, float b)
{
    return a - b;
}

float dividir(float a, float b)
{
    return a / b;
}

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

float potencia(float base, int exp)
{
    float resultado = 1.0;
    int exp_pos = exp;
    int i;

    if (exp_pos < 0) {
        exp_pos = -exp_pos;
    }

    for (i = 0; i < exp_pos; i++) {
        resultado = multiplicar(resultado, base);
    }

    if (exp < 0) {
        return 1.0 / resultado;
    }

    return resultado;
}

int menu()
{
    int op;
    printf("\nCALCULADORA\n");
    printf("1 - Adicao\n");
    printf("2 - Subtracao\n");
    printf("3 - Divisao\n");
    printf("4 - Multiplicacao\n");
    printf("5 - Potencia\n");
    printf("0 - Sair\n");
    printf("Escolha uma opcao: ");
    scanf("%d", &op);
    return op;
}

// PRINCIPAL
int main()
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int opcao;
    float n1, n2, res;
    int exp;

    do {
        opcao = menu();

        switch (opcao) {
            case 1:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &n1);
                printf("Digite o segundo numero: ");
                scanf("%f", &n2);
                res = somar(n1, n2);
                printf("Resultado: %.2f\n", res);
                break;

            case 2:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &n1);
                printf("Digite o segundo numero: ");
                scanf("%f", &n2);
                res = subtrair(n1, n2);
                printf("Resultado: %.2f\n", res);
                break;

            case 3:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &n1);
                do {
                    printf("Digite o segundo numero (diferente de 0): ");
                    scanf("%f", &n2);
                    if (n2 == 0) printf("Divisao por zero nao permitida.\n");
                } while (n2 == 0);
                res = dividir(n1, n2);
                printf("Resultado: %.2f\n", res);
                break;

            case 4:
                printf("\nDigite o primeiro numero: ");
                scanf("%f", &n1);
                printf("Digite o segundo numero (inteiro): ");
                scanf("%f", &n2);
                res = multiplicar(n1, n2);
                printf("Resultado: %.2f\n", res);
                break;

            case 5:
                printf("\nDigite a base (X): ");
                scanf("%f", &n1);
                printf("Digite o expoente inteiro (Y): ");
                scanf("%d", &exp);
                res = potencia(n1, exp);
                printf("Resultado: %.4f\n", res);
                break;

            case 0:
                printf("\nEncerrando a calculadora...\n");
                break;

            default:
                printf("\nOpcao invalida! Tente novamente.\n");
                break;
        }

    } while (opcao != 0);

    return 0;
}