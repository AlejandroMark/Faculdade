/* Crie um programa em C que leia a idade de uma pessoa e informe a sua classe eleitoral:
 não eleitor (abaixo de 16 anos);
 eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
 eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive).*/

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int idade;

    printf("Informe a idade: ");
    scanf("%d", &idade);

    if (idade < 16) {
        printf("Classe: Não eleitor\n");
    } 
    else if (idade >= 18 && idade < 65) {
        printf("Classe: Eleitor obrigatório\n");
    } 
    else {
        printf("Classe: Eleitor facultativo\n");
    }

    return 0;
}