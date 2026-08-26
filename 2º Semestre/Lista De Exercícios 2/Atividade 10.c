/* Criar um programa em C que leia o um número inteiro entre 1 e 7 e escreva o dia da
semana correspondente. Caso o usuário digite um número fora desse intervalo, deverá
aparecer uma mensagem informando que não existe dia da semana com esse número. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() 
{
    SetConsoleOutputCP(65001);

    int dia;

    printf("Digite um número de 1 a 7: ");
    scanf("%d", &dia);

    switch (dia) {
        case 1:
            printf("Domingo\n");
            break;
        case 2:
            printf("Segunda-feira\n");
            break;
        case 3:
            printf("Terça-feira\n");
            break;
        case 4:
            printf("Quarta-feira\n");
            break;
        case 5:
            printf("Quinta-feira\n");
            break;
        case 6:
            printf("Sexta-feira\n");
            break;
        case 7:
            printf("Sábado\n");
            break;
        default:
            printf("Não existe dia da semana com esse número.\n");
            break;
    }

    return 0;
}