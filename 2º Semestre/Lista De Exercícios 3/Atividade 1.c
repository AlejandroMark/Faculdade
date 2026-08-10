/* Implemente um programa que imprima todos os números inteiros de 100 a 1 (em ordem
decrescente). */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int i;

    for (i = 100; i >= 1; i--) 
    {
        printf("%d\n", i);
    }

    return 0;
}