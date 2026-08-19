/* Faça um algoritmo que dado as notas de cada um dos alunos do 2º Período do curso de
Bacharel de Sistemas de Informação, gere uma serie de estatísticas. Para tanto, serão
fornecidos a matrícula, a nota e o sexo de cada aluno. Quando for informado uma matrícula
negativa (ou zero), encerrar a leitura das informações. Deseja-se as seguintes informações
estatísticas:
- Quantos homens existem na turma ?
- Quantas mulheres existem na turma ?
- Qual é a média das notas ?
- Quantos alunos DR existem na turma ?
- Quantos alunos DI existem na turma ?
- Qual a % de alunos DB, DR e DI na turma ?
- Qual a % de homens DB, DR e DI na turma ?
- Qual a % de mulheres DB, DR e DI na turma ?
Definições:
DB – Desenvolvendo-se bem: nota entre 80 e 100
DR – Desenvolvendo-se regularmente: nota entre 60 e 79
DI – Desenvolvendo-se insuficiente: nota menor que 60 */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{ 
    // Para acentuação
    SetConsoleOutputCP(65001);

    int matricula;
    float nota;
    char sexo;

    int total = 0, homens = 0, mulheres = 0;
    int total_db = 0, total_dr = 0, total_di = 0;

    int h_db = 0, h_dr = 0, h_di = 0;
    int m_db = 0, m_dr = 0, m_di = 0;

    float soma_notas = 0;

    while (1) 
    {
        printf("Digite a matricula (0 ou negativo para sair): ");
        scanf("%d", &matricula);

        if (matricula <= 0) {
            break;
        }

        do {
            printf("Digite a nota (0 a 100): ");
            scanf("%f", &nota);
            if (nota < 0 || nota > 100) printf("Nota invalida.\n");
        } while (nota < 0 || nota > 100);

        do {
            printf("Digite o sexo (M/F): ");
            scanf(" %c", &sexo);
            if (sexo != 'M' && sexo != 'm' && sexo != 'F' && sexo != 'f') {
                printf("Opção invalida.\n");
            }
        } while (sexo != 'M' && sexo != 'm' && sexo != 'F' && sexo != 'f');

        total++;
        soma_notas += nota;

        if (sexo == 'M' || sexo == 'm') {
            homens++;
            if (nota >= 80) {
                total_db++;
                h_db++;
            } else if (nota >= 60) {
                total_dr++;
                h_dr++;
            } else {
                total_di++;
                h_di++;
            }
        } else {
            mulheres++;
            if (nota >= 80) {
                total_db++;
                m_db++;
            } else if (nota >= 60) {
                total_dr++;
                m_dr++;
            } else {
                total_di++;
                m_di++;
            }
        }
        printf("\n");
    }

    if (total > 0) {
        printf("\n--- ESTATISTICAS ---\n");
        printf("Total de homens: %d\n", homens);
        printf("Total de mulheres: %d\n", mulheres);
        printf("Media das notas: %.2f\n", soma_notas / total);
        printf("Alunos DR: %d\n", total_dr);
        printf("Alunos DI: %d\n", total_di);
        
        printf("\n%% Turma DB: %.2f%%\n", ((float)total_db / total) * 100);
        printf("%% Turma DR: %.2f%%\n", ((float)total_dr / total) * 100);
        printf("%% Turma DI: %.2f%%\n", ((float)total_di / total) * 100);

        if (homens > 0) {
            printf("\n%% Homens DB: %.2f%%\n", ((float)h_db / homens) * 100);
            printf("%% Homens DR: %.2f%%\n", ((float)h_dr / homens) * 100);
            printf("%% Homens DI: %.2f%%\n", ((float)h_di / homens) * 100);
        } else {
            printf("\nNenhum homem cadastrado.\n");
        }

        if (mulheres > 0) {
            printf("\n%% Mulheres DB: %.2f%%\n", ((float)m_db / mulheres) * 100);
            printf("%% Mulheres DR: %.2f%%\n", ((float)m_dr / mulheres) * 100);
            printf("%% Mulheres DI: %.2f%%\n", ((float)m_di / mulheres) * 100);
        } else {
            printf("\nNenhuma mulher cadastrada.\n");
        }
    } else {
        printf("Nenhum aluno cadastrado.\n");
    }

    return 0;
}