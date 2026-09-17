#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define MAX 100

void listar(int *vetor, int quant) {
    int i;
    for (i = 0; i < quant; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n\n");
}

int pesquisar(int *vetor, int quant, int pesq) {
    int i;
    for (i = 0; i < quant; i++) {
        if (vetor[i] == pesq) {
            return i;
        }
    }
    return -1;
}

void inserir(int *vetor, int *quant, int valor) {
    if (*quant < MAX) {
        vetor[*quant] = valor;
        (*quant)++;
    }
}

void remover(int *vetor, int *quant, int pos) {
    int i;
    if (pos >= 0 && pos < *quant) {
        for (i = pos; i < *quant - 1; i++) {
            vetor[i] = vetor[i + 1];
        }
        (*quant)--;
    }
}

void uniao(int *A, int qntA, int *B, int qntB, int *C, int *qntC) {
    int i;
    *qntC = 0;

    for (i = 0; i < qntA; i++) {
        if (pesquisar(C, *qntC, A[i]) == -1) {
            inserir(C, qntC, A[i]);
        }
    }

    for (i = 0; i < qntB; i++) {
        if (pesquisar(C, *qntC, B[i]) == -1) {
            inserir(C, qntC, B[i]);
        }
    }
}

void intersecao(int *A, int qntA, int *B, int qntB, int *C, int *qntC) {
    int i;
    *qntC = 0;

    for (i = 0; i < qntA; i++) {
        if (pesquisar(B, qntB, A[i]) != -1) {
            if (pesquisar(C, *qntC, A[i]) == -1) {
                inserir(C, qntC, A[i]);
            }
        }
    }
}

void diferenca(int *A, int qntA, int *B, int qntB, int *C, int *qntC) {
    int i;
    *qntC = 0;

    for (i = 0; i < qntA; i++) {
        if (pesquisar(B, qntB, A[i]) == -1) {
            if (pesquisar(C, *qntC, A[i]) == -1) {
                inserir(C, qntC, A[i]);
            }
        }
    }
}

void diferencaSimetrica(int *A, int qntA, int *B, int qntB, int *C, int *qntC) {
    int i;
    *qntC = 0;

    for (i = 0; i < qntA; i++) {
        if (pesquisar(B, qntB, A[i]) == -1) {
            if (pesquisar(C, *qntC, A[i]) == -1) {
                inserir(C, qntC, A[i]);
            }
        }
    }

    for (i = 0; i < qntB; i++) {
        if (pesquisar(A, qntA, B[i]) == -1) {
            if (pesquisar(C, *qntC, B[i]) == -1) {
                inserir(C, qntC, B[i]);
            }
        }
    }
}

int menu() {
    int op;
    printf("\n----- MENU DE OPERAÇÕES -----");
    printf("\n0 - Sair");
    printf("\n1 - União (A U B)");
    printf("\n2 - Interseção (A ∩ B)");
    printf("\n3 - Diferença (B - A)");
    printf("\n4 - Diferença (A - B)");
    printf("\n5 - Diferença Simétrica (A ∆ B)");
    printf("\n\nInsira a opção equivalente à operação que deseja realizar: ");
    scanf("%d", &op);
    return op;
}

int main() {
    SetConsoleOutputCP(65001);

    int conjA[MAX] = {3, 5, 1, 4};
    int conjB[MAX] = {2, 1, 3, 9, 7, 10};
    int qntdA = 4, qntdB = 6, opcao;
    int conjRes[MAX];
    int qntdRes = 0;

    printf("Conjunto A: ");
    listar(conjA, qntdA);

    printf("Conjunto B: ");
    listar(conjB, qntdB);

    do {
        opcao = menu();
        switch (opcao) {
            case 0:
                break;

            case 1:
                printf("\nUnião de A e B: ");
                uniao(conjA, qntdA, conjB, qntdB, conjRes, &qntdRes);
                listar(conjRes, qntdRes);
                break;

            case 2:
                printf("\nInterseção de A e B: ");
                intersecao(conjA, qntdA, conjB, qntdB, conjRes, &qntdRes);
                listar(conjRes, qntdRes);
                break;

            case 3:
                printf("\nDiferença de B - A: ");
                diferenca(conjB, qntdB, conjA, qntdA, conjRes, &qntdRes);
                listar(conjRes, qntdRes);
                break;

            case 4:
                printf("\nDiferença de A - B: ");
                diferenca(conjA, qntdA, conjB, qntdB, conjRes, &qntdRes);
                listar(conjRes, qntdRes);
                break;

            case 5:
                printf("\nDiferença Simétrica de A ∆ B: ");
                diferencaSimetrica(conjA, qntdA, conjB, qntdB, conjRes, &qntdRes);
                listar(conjRes, qntdRes);
                break;

            default:
                printf("\nOpção inválida! Tente novamente.\n");
        }
    } while (opcao != 0);

    return 0;
}