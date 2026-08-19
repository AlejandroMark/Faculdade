/* Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Atenção:
só existe fatorial de números maiores que zero (coloque validação para isso). */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int num; 
    int fat = 1;
    int i = 1;

    printf("Número Que Deseja Fatoriar: ");
    scanf("%d", &num);

    while (num < 0)
    {
        printf("Informe Um Número Maior Que 0: ");
        scanf("%d", &num);
    }
    
    while (i <= num )
    {
        fat = fat * i;
        i++;
    }
    printf("Fatoiral de %d é igual a %d\n", num, fat);
    
    return 0;
}