/* Implemente um programa em C que dada a idade de uma pessoa, determine sua
classificação segundo as informações:
- maior de idade;
- menor de idade;
- pessoa idosa (idade superior ou igual a 65 anos). */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int idade;

    printf("Informe Sua Idade: ");
    scanf("%d", &idade);

    if (idade >= 65) {
        printf("Pessoa idosa\n");
    }
    else if (idade >= 18) {
        printf("Maior de idade\n");
    }
    else {
        printf("Menor de idade\n");
    }

    return 0;
}