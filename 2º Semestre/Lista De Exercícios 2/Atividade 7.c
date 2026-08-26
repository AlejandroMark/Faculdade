/* Implemente um programa em C que leia as três notas semestrais de um aluno e determine
a média da nota semestral. Através da média calculada o algoritmo deve imprimir a
seguinte mensagem: Aprovado, Reprovado ou em Prova Final (a média é 7 para
Aprovação, menor que 3 para Reprovação e as demais em Prova Final). */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() 
{
    SetConsoleOutputCP(65001);

    float n1, n2, n3, media;

    printf("Digite a primeira nota: ");
    scanf("%f", &n1);

    printf("Digite a segunda nota: ");
    scanf("%f", &n2);

    printf("Digite a terceira nota: ");
    scanf("%f", &n3);

    media = (n1 + n2 + n3) / 3.0;

    printf("\nMédia: %.2f\n", media);

    if (media >= 7.0) {
        printf("Situação: Aprovado\n");
    } 
    else if (media < 3.0) {
        printf("Situação: Reprovado\n");
    } 
    else {
        printf("Situação: Em Prova Final\n");
    }

    return 0;
}