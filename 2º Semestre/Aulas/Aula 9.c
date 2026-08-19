#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 

// Para os números aleatórios 
// ########## JOGO DE CRAPS  ################### 
// Jogar os dados. O resto da divisão por 6 é 
//    um número de entre 0 e 5, por isso soma-se 1 

int lancarDado(){ 
    return ( rand() % 6) + 1; 
} 

int jogarDados(){ 
    int d1, d2, soma; 
    printf("\n\nVamos jogar os dados\n"); 
    system("PAUSE"); 
    d1 = lancarDado(); 
    d2 = lancarDado(); 
    soma = d1 + d2; 
    printf("Dado 1: %d\nDado 2: %d\n\n", d1, d2); 
    printf("SOMA: %d\n", soma); 
    printf("---------------------\n\n"); 
    return soma; 
}

int main(){ 
    // SEMENTE DOS NUMEROS ALEATÓRIOS. Usa a hora local 
    srand( (unsigned)  time(NULL) ); 

    // TESTE
    int i;
    for (i=1; i <= 10; i++) {
        printf(" %d  ",   jogarDados()   );

    }

}