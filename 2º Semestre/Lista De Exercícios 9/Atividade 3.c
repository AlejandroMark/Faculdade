#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 200

FILE * abrirArquivo(char * nome, char * modo) {
    FILE * arquivo;
    arquivo = fopen(nome, modo);
    if (arquivo == NULL) {
        printf("ERRO ao abrir arquivo");
        exit(1);
    }
    return arquivo;
}

void inserir(int * vetor, int * qtde, int elem) {
    vetor[*qtde] = elem;
    (*qtde)++;
}

void gravarVetor(char * nomeArq, int * vetor, int qtde) {
    FILE * arq;
    int i;

    arq = abrirArquivo(nomeArq, "w");
    for (i = 0; i < qtde; i++) {
        fprintf(arq, "%d\n", vetor[i]);
    }
    fclose(arq);
}

int main() {
    FILE * arq;
    int vetLEDS[MAX], vetLETER[MAX], vetRobotica[MAX];
    int qtdeLEDS = 0, qtdeLETER = 0, qtdeRobotica = 0;
    int matricula;
    char projetos[100];

    arq = abrirArquivo("ex3_alunos.txt", "r");

    while (!feof(arq)) {
        if (fscanf(arq, "%d", &matricula) == 1) {
            strcpy(projetos, "");
            fscanf(arq, "%[^\n]s", projetos);

            if (strstr(projetos, "LEDS") != NULL) {
                inserir(vetLEDS, &qtdeLEDS, matricula);
            }
            if (strstr(projetos, "LETER") != NULL) {
                inserir(vetLETER, &qtdeLETER, matricula);
            }
            if (strstr(projetos, "Robótica") != NULL) {
                inserir(vetRobotica, &qtdeRobotica, matricula);
            }
        }
    }

    fclose(arq);

    gravarVetor("leds.txt", vetLEDS, qtdeLEDS);
    gravarVetor("leter.txt", vetLETER, qtdeLETER);
    gravarVetor("robotica.txt", vetRobotica, qtdeRobotica);

    printf("FIM DO PROGRAMA.");
    return 0;
}