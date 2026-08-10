/* Para vários tributos, a base de cálculo é o salário mínimo. Fazer um programa em
Linguagem C que leia o valor do salário mínimo e o valor do salário de uma pessoa.
Calcular e imprimir quantos salários mínimos essa pessoa ganha. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main()
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float salarioMinimo, salarioPessoa, quantidade;

    printf("Digite o valor do salário mínimo: R$ ");
    scanf("%f", &salarioMinimo);

    printf("Digite o valor do salário da pessoa: R$ ");
    scanf("%f", &salarioPessoa);

    quantidade = salarioPessoa / salarioMinimo;

    printf("\nA pessoa ganha %.2f salários mínimos.\n", quantidade);

    return 0;
}