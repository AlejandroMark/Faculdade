/* Em uma competição de ginástica, cada atleta recebe votos de cinco jurados. As notas são
de 0 a 10. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
restantes. Você deve fazer um programa que receba as notas dos cinco jurados
alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a
descrição acima informada (retirar a melhor e a pior nota e depois calcular a média com as
notas restantes). As notas não são informadas ordenadas. Ao final, mostrar a média das
notas, a maior e a menor nota. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() 
{
    SetConsoleOutputCP(65001);

    float nota, maior, menor;
    float soma = 0.0, media;
    int i;

    for (i = 1; i <= 5; i++) 
    {
        do {
            printf("Digite a nota do %dº jurado (0 a 10): ", i);
            scanf("%f", &nota);

            if (nota < 0 || nota > 10) {
                printf("Nota inválida! Digite um valor entre 0 e 10.\n");
            }
        } while (nota < 0 || nota > 10);

        soma += nota;

        if (i == 1) {
            maior = nota;
            menor = nota;
        } else {
            if (nota > maior) {
                maior = nota;
            }
            if (nota < menor) {
                menor = nota;
            }
        }
    }

    media = (soma - maior - menor) / 3.0;

    printf("\n--- RESULTADO ---\n");
    printf("Maior nota: %.2f\n", maior);
    printf("Menor nota: %.2f\n", menor);
    printf("Média final do atleta: %.2f\n", media);

    return 0;
}