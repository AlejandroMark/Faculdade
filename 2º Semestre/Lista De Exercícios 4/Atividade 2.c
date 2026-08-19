/* Faça um programa com funções em C que leia o preço de um produto qualquer (maior que zero) e a forma de pagamento 
(à vista ou à prazo, pode ser char ou int) e calcule o preço final desse produto da seguinte forma:
 O preço do produto à vista tem desconto de 10%.
O preço do produto à prazo tem acréscimo de 10%. 
Depois, leia a quantidade (maior que zero) desse produto que será comprada e informe o valor total da compra. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#define _USE_MATH_DEFINES 

float lerPreco() {
    float preco;
    do {
        printf("Digite o preço do produto: ");
        scanf("%f", &preco);
        if (preco <= 0) {
            printf("Preço inválido!\n");
        }
    } while (preco <= 0);

    return preco;
}

int lerFormaPagamento() {
    int opcao;
    do {
        printf("\nEscolha a forma de pagamento:\n");
        printf("1 - À vista (10%% de desconto)\n");
        printf("2 - À prazo (10%% de acréscimo)\n");
        printf("Opção: ");
        scanf("%d", &opcao);

        if (opcao != 1 && opcao != 2) {
            printf("Opção inválida! Escolha 1 ou 2.\n");
        }
    } while (opcao != 1 && opcao != 2);

    return opcao;
}

float calcPrecoFinal(float preco, int forma) {
    float precoFinal;
    
    if (forma == 1) {
        precoFinal = preco * 0.90;
    } else {
        precoFinal = preco * 1.10;
    }

    return precoFinal;
}

int lerQuantidade() {
    int qtd;
    do {
        printf("\nDigite a quantidade comprada: ");
        scanf("%d", &qtd);
        if (qtd <= 0) {
            printf("Quantidade inválida!\n");
        }
    } while (qtd <= 0);

    return qtd;
}

void imprimirResumo(int qtd, float precoAjustado, float total) {
    printf("Quantidade de itens: %d\n", qtd);
    printf("Preço final por unidade: R$ %.2f\n", precoAjustado);
    printf("Valor total a pagar: R$ %.2f\n", total);
}

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    float precoBase, precoAjustado, valorTotal;
    int formaPagamento, quantidade;

    // Fluxo do programa com as chamadas de funções
    precoBase = lerPreco();
    formaPagamento = lerFormaPagamento();
    
    precoAjustado = calcPrecoFinal(precoBase, formaPagamento);
    
    quantidade = lerQuantidade();
    valorTotal = precoAjustado * quantidade;

    imprimirResumo(quantidade, precoAjustado, valorTotal);

    return 0;
}