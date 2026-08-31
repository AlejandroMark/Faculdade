#include <stdio.h> 
#include <stdlib.h> 
#include <ctype.h>

#define MAX 1000

int lerIdade() {
    int idade;
    do {
        printf("Idade: ");
        scanf("%d", &idade);
    } while ( idade <= 0 );
    return idade;
}


void inserir(int * vet, int *q) {
    char cont;
    do {
        vet[*q]= lerIdade();
        (*q)++;
        printf("Deseja continuar? ");
        scanf(" %c", &cont);
    } while ( toupper(cont) == 'S');
}


void listar( int * vet, int qtde) {
    int i;
    for ( i=0; i < qtde; i++ ) {
        printf("%d   ", vet[i] );
    }
}

int main(){ 

    int vetor[MAX];
    int qtde = 0;

    // INSERIR
    inserir(vetor, &qtde);

    listar(vetor,qtde);

    return 0;
}