#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE * abrirArquivo(char * nome, char * modo) {
    FILE * arquivo;
    arquivo = fopen(nome, modo);
    if (arquivo == NULL) {
        printf("ERRO ao abrir arquivo");
        exit(1);
    }
    return arquivo;
}

void minuscula(char * str) {
    int i;
    int tam = strlen(str);
    for (i = 0; i < tam; i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            str[i] = str[i] + 32;
        }
    }
}

int pesquisar(char vet[][50], int qtde, char * pesq) {
    int i;
    char aux[100];

    strcpy(aux, pesq);
    minuscula(aux);

    for (i = 0; i < qtde; i++) {
        if (strcmp(vet[i], aux) == 0) {
            return i;
        }
    }
    return -1;
}

int main() {
    FILE * arq;
    FILE * arqSaida;
    char palavra[100];
    int pos;

    char palavrasProibidas[100][50] = {
        "sexo", "erótico", "golpe", "ladrão", "rapariga",
        "rebelião", "darth", "vader", "skywalker", "jedi", "flamengo"
    };

    arq = abrirArquivo("ex1_input.txt", "r");
    arqSaida = abrirArquivo("ex1_output.txt", "w");

    while (!feof(arq)) {
        if (fscanf(arq, "%s", palavra) == 1) {
            pos = pesquisar(palavrasProibidas, 11, palavra);

            if (pos >= 0) {
                fprintf(arqSaida, "**** ");
            } else {
                fprintf(arqSaida, "%s ", palavra);
                printf("%s ", palavra);
            }
        }
    }

    printf("\nFIM DO PROGRAMA.");
    fclose(arq);
    fclose(arqSaida);
    return 0;
}