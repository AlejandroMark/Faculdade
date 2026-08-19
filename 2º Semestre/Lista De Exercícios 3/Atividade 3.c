/* Criar um programa que leia a quantidade de números a serem lidos.
Depois, leia os números inteiros até essa quantidade e imprima o menor deles.
Suponha que todos os números lidos serão positivos, então coloque a validação desses números.*/

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int qtn, num, menor;
    int i = 1;

    do {
        printf("Informe A Quantidade De Números A Ser Lidos: ");
        scanf("%d", &qtn);
        if (qtn <= 0) {
            printf("Quantidade inválida! Informe um número maior que 0.\n");
        }
    } while (qtn <= 0);

    while (i <= qtn) 
    {
        do {
            printf("Informe o %dº número positivo: ", i);
            scanf("%d", &num);
            if (num <= 0) {
                printf("Número inválido! Digite apenas números positivos maiores que 0.\n");
            }
        } while (num <= 0);

        if (i == 1) {
            menor = num;
        } 
        else if (num < menor) {
            menor = num;
        }

        i++;
    }

    printf("\nO menor número digitado foi: %d\n", menor);

    return 0;
}