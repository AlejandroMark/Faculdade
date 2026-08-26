/* Criar um programa em C que leia um número inteiro entre 1 e 12 e escrever o mês
correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer
uma mensagem informando que não existe mês com este número. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() 
{
    SetConsoleOutputCP(65001);

    int mes;

    printf("Digite um número de 1 a 12: ");
    scanf("%d", &mes);

    switch (mes) {
        case 1:
            printf("Janeiro\n");
            break;
        case 2:
            printf("Fevereiro\n");
            break;
        case 3:
            printf("Março\n");
            break;
        case 4:
            printf("Abril\n");
            break;
        case 5:
            printf("Maio\n");
            break;
        case 6:
            printf("Junho\n");
            break;
        case 7:
            printf("Julho\n");
            break;
        case 8:
            printf("Agosto\n");
            break;
        case 9:
            printf("Setembro\n");
            break;
        case 10:
            printf("Outubro\n");
            break;
        case 11:
            printf("Novembro\n");
            break;
        case 12:
            printf("Dezembro\n");
            break;
        default:
            printf("Não existe mês com este número.\n");
            break;
    }

    return 0;
}