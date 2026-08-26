/* Faça um programa que receba o código e a quantidade de um produto comprado. Calcule
e mostre:
 O preço unitário do produto comprado, conforme Tabela 1;
 O valor total da nota;
 O valor de desconto, conforme Tabela 2, e aplicado sobre o valor total;
 O valor total depois do desconto.
TABELA 1
Código Preço
1 a 10 R$ 10,00
11 a 20 R$ 15,00
21 a 30 R$ 20,00
31 a 40 R$ 30,00
TABELA 2
Valor total (R$) Desconto
Até 250 5%
Entre 250,00 e 500 10%
De 500 para cima 15% */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() 
{
    SetConsoleOutputCP(65001);

    int codigo, qtd;
    float preco_unit, total_bruto, desconto, total_final;
    float perc_desconto;

    printf("Digite o código do produto (1 a 40): ");
    scanf("%d", &codigo);

    printf("Digite a quantidade comprada: ");
    scanf("%d", &qtd);

    // Tabela 1: Preço unitário pelo código
    if (codigo >= 1 && codigo <= 10) {
        preco_unit = 10.0;
    } 
    else if (codigo >= 11 && codigo <= 20) {
        preco_unit = 15.0;
    } 
    else if (codigo >= 21 && codigo <= 30) {
        preco_unit = 20.0;
    } 
    else if (codigo >= 31 && codigo <= 40) {
        preco_unit = 30.0;
    } 
    else {
        printf("\nCódigo de produto inválido!\n");
        return 0;
    }

    // Cálculo do total bruto
    total_bruto = preco_unit * qtd;

    // Tabela 2: Desconto pelo valor total
    if (total_bruto <= 250.0) {
        perc_desconto = 0.05; // 5%
    } 
    else if (total_bruto <= 500.0) {
        perc_desconto = 0.10; // 10%
    } 
    else {
        perc_desconto = 0.15; // 15%
    }

    desconto = total_bruto * perc_desconto;
    total_final = total_bruto - desconto;

    printf("\n--- NOTA FISCAL ---\n");
    printf("Preço unitário: R$ %.2f\n", preco_unit);
    printf("Valor total da nota: R$ %.2f\n", total_bruto);
    printf("Valor do desconto: R$ %.2f\n", desconto);
    printf("Valor final a pagar: R$ %.2f\n", total_final);

    return 0;
}