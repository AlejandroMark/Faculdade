/* Implemente um programa em C que leia um número e informe se ele é divisível por 10, por
5 ou por 2 ou se não é divisível por nenhum deles. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int num;

    printf("Informe Um Número: ");
    scanf("%d", &num);

    if (num % 10 == 0) {
        printf("O número %d é divisível por 10.\n", num);
    } 
    else if (num % 5 == 0) {
        printf("O número %d é divisível por 5.\n", num);
    } 
    else if (num % 2 == 0) {
        printf("O número %d é divisível por 2.\n", num);
    } 
    else {
        printf("O número %d não é divisível por 10, por 5 e nem por 2.\n", num);
    }

    return 0;
}