/* Construir um programa em C que leia dois números e efetue a adição. Caso o valor
somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8. Caso o
valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int valor1, valor2, ad;

    printf("Informe Um Valor:");
    scanf("%d", &valor1);

    printf("Informe Um Valor:");
    scanf("%d", &valor2);

    ad = valor1 + valor2;
    printf("A Soma Dos Valores É De: %d\n", ad);

    if (ad > 20){
        ad = ad + 8;
        printf("O Resultado De Maior Que 20 É: %d\n", ad);
    }
    else if (ad <= 20){
        ad = ad -5;
        printf("O Resultado De Menor Ou Igual A 20 É: %d\n", ad);        
    }
    
    return 0;
}