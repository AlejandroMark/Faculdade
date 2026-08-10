/* Implemente um programa que imprima todos os números múltiplos de 5, no intervalo fechado de 1 a 500. */

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

    for (i = 5; i <= 500; i = i + 5) 
    {
        printf("%d\n", i);
    }

    return 0;
}