#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() {

    // Para acentuação
    SetConsoleOutputCP(65001);

    int i, ini, final;

    printf("Início: ");
    scanf("%d", &ini);

    printf("Fim: ");
    scanf("%d", &final);

    printf("Números divisíveis por 3 entre %d e %d\n\n", ini, final);
    for ( i = ini; i <= final; i++ ) {
        if ( i % 3 == 0 ) {
            printf("%d  ", i);

        }

    }





    return 0;
}