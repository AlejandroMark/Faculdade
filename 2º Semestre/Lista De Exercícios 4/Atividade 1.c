/* Faça um programa com funções em C para ler a matrícula do aluno e suas três notas. Valide
os dados de entrada. A matrícula deve ser maior que zero e as notas entre 0 e 10. Calcule a
média final do aluno e imprima: “APROVADO” se a média for maior ou igual a 7;
“REPROVADO” se a média for menor que 6; e “PROVA FINAL” se a média estiver entre 6 e 7.
Faça uma função para cada operação: ler e validar a matrícula; ler e validar as notas; calcular a
média e imprimir a mensagem. */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#define _USE_MATH_DEFINES

// FUNÇÕES
int lerMatricula() {
    int matricula;
    do {
        printf("Informe A Matricula: ");
        scanf("%d", &matricula);
        if (matricula <= 0) {
            printf("Matrícula inválida!\n");
        }
    } while (matricula <= 0);

    return matricula;
}

void lerNotas(float *n1, float *n2, float *n3) {
    do {
        printf("Informe A Primeira Nota: ");
        scanf("%f", n1);
        if (*n1 < 0 || *n1 > 10) {
            printf("Nota inválida!\n");
        }
    } while (*n1 < 0 || *n1 > 10);

    do {
        printf("Informe A Segunda Nota: ");
        scanf("%f", n2);
        if (*n2 < 0 || *n2 > 10) {
            printf("Nota inválida!\n");
        }
    } while (*n2 < 0 || *n2 > 10);

    do {
        printf("Informe A Terceira Nota: ");
        scanf("%f", n3);
        if (*n3 < 0 || *n3 > 10) {
            printf("Nota inválida!\n");
        }
    } while (*n3 < 0 || *n3 > 10);
}

float calcMedia(float n1, float n2, float n3) {
    float media;
    media = (n1 + n2 + n3) / 3.0;
    return media;
}

void imprimirResultado(float media) {
    printf("Média Final: %.2f\n", media);
    
    if (media >= 7.0) {
        printf("Aprovado\n");
    } else if (media < 6.0) {
        printf("Reprovado\n");
    } else {
        printf("Prova Final\n");
    }
}

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int mat;
    float nota1, nota2, nota3, mediaFinal;

    mat = lerMatricula();
    lerNotas(&nota1, &nota2, &nota3);
    
    mediaFinal = calcMedia(nota1, nota2, nota3);
    
    printf("Resultado (Matrícula: %d)\n", mat);
    imprimirResultado(mediaFinal);

    return 0;
}