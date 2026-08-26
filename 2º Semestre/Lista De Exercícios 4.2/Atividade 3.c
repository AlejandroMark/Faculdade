/* Faça uma função que dado dois valores (X, Y) retorne X * Y, entretanto não é
permitido usar o operador de produto. ( * ).
Sugestão: Use o operador de soma com um comando de repetição */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int multiplicar(int x, int y)
{
    int resultado = 0;
    int vezes = y;
    int positivo = 1;

    if (vezes < 0) {
        vezes = -vezes;
        positivo = -positivo;
    }

    for (int i = 0; i < vezes; i++) {
        resultado += x;
    }

    if (positivo < 0) {
        resultado = -resultado;
    }

    return resultado;
}

int main()
{
    SetConsoleOutputCP(65001);

    int num1, num2, res;

    printf("Digite o primeiro número: ");
    scanf("%d", &num1);

    printf("Digite o segundo número: ");
    scanf("%d", &num2);

    res = multiplicar(num1, num2);

    printf("\nResultado de %d x %d = %d\n", num1, num2, res);

    return 0;
}