#include <stdio.h>
#include <stdlib.h>

#define _USE_MATH_DEFINES 
#include <math.h> 

float lerNota () {
    float nota;

    do {
        printf("Digite uma nota: ");
        scanf("%f", &nota);

    } while ( ( nota < 0 ) || (nota > 10) );

    return nota;
}


float calcMedia( float n1 , float n2 , float n3 ) { 
    float media;
    media = ( n1 + n2 + n3 ) / 3;
    return media;
} 

void mostrarResultado( float m) {

    if ( m < 6 ) {
        printf("REPROVADO.\n");
    } else {
        printf("APROVADO.\n");
    } 

    printf("Média: %.2f", m);

}


// PRINCIPAL
int main() {
    float nota1, nota2, nota3;
    float media;

    nota1 = lerNota();
    nota2 = lerNota();
    nota3 = lerNota();

    media = calcMedia(nota1, nota2, nota3);

    mostrarResultado(media);

   return 0;
}