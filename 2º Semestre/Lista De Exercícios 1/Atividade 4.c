/* Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas
vendas oferecendo desconto. Faça um programa em C que possa entrar com o valor de
um produto e imprima o novo valor tendo em vista que o desconto foi de 9%. Além disso,
imprima o valor do desconto. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float valorProduto, valorDesconto, novoValor;

    printf("Informe o valor do produto: R$ ");
    scanf("%f", &valorProduto);

    valorDesconto = valorProduto * 0.09;
    novoValor = valorProduto - valorDesconto;

    printf("\nValor do desconto (9%%): R$ %.2f\n", valorDesconto);
    printf("Novo valor do produto: R$ %.2f\n", novoValor);

    return 0;
}