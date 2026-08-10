/* Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o
preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.  */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main()
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float km, dias, valorTotal;

    printf("Digite a quantidade de km percorridos: ");
    scanf("%f", &km);

    printf("Digite a quantidade de dias que o carro foi alugado: ");
    scanf("%f", &dias);

    valorTotal = (dias * 60) + (km * 0.15);

    printf("\nValor total a pagar: R$ %.2f\n", valorTotal);

    return 0;
}