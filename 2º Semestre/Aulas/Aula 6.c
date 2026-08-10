#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    float nota, soma, media;
    int cont;
    char continuar;

    // Para acentuação
    SetConsoleOutputCP(65001);

    continuar = 'S';
    soma = 0;
    cont = 0;
    while ( continuar == 'S') {
               
        cont++;     // cont = cont + 1

        // Leitura e validação da nota
        printf("Nota %d\n", cont);
        do {
            printf("Digite uma nota: ");
            scanf("%f", &nota);
        } while ( nota < 0  ||  nota > 10 ) ;

        soma = soma + nota;        

        printf("Deseja continuar? ");
        scanf(" %c", &continuar);
    }

    media = soma / cont;
    printf("Sua média é %.2f\n", media);

    if ( media < 6.0 ) {
        printf("REPROVADO!");
    } else {
        printf("APROVADO!");
    }


    return 0;
}