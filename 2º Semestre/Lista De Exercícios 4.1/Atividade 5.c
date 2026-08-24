/* DESAFIO: Cassino. Altere o Jogo de Craps da questão anterior para que o jogador possa
apostar. Ele começa com R$ 100,00. No início de cada rodada ele informa quanto quer
apostar. Se perder, perde esse valor. Se ganhar, ganha o dobro do que apostou. No final de
cada rodada informe o total que ele tem em dinheiro e pergunte se quer continuar jogando ou
se quer parar. */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <math.h>

int lancarDado()
{
    return (rand() % 6) + 1;
}

int jogarDados()
{
    int d1, d2, soma;
    printf("\nVamos jogar os dados\n");
    system("PAUSE");
    d1 = lancarDado();
    d2 = lancarDado();
    soma = d1 + d2;
    printf("Dado 1: %d\nDado 2: %d\n\n", d1, d2);
    printf("SOMA: %d\n", soma);
    printf("---------------------\n\n");
    return soma;
}

int main()
{
    SetConsoleOutputCP(65001);

    srand((unsigned)time(NULL));

    float saldo = 100.0, aposta;
    int soma, ponto, opcao;

    do {
        printf("\nSaldo atual: R$ %.2f\n", saldo);

        do {
            printf("Quanto deseja apostar? R$ ");
            scanf("%f", &aposta);
            if (aposta <= 0 || aposta > saldo) {
                printf("Valor invalido! Aposte entre R$ 0.01 e R$ %.2f\n", saldo);
            }
        } while (aposta <= 0 || aposta > saldo);

        soma = jogarDados();

        if (soma == 7 || soma == 11) {
            printf("Voce ganhou!\n");
            saldo += aposta;
        } 
        else if (soma == 2 || soma == 3 || soma == 12) {
            printf("CRAPS! Voce perdeu.\n");
            saldo -= aposta;
        } 
        else {
            ponto = soma;
            printf("Seu PONTO e: %d\n", ponto);
            printf("Continue jogando ate tirar %d. Se tirar 7, voce perde.\n", ponto);

            while (1) {
                soma = jogarDados();

                if (soma == ponto) {
                    printf("Voce tirou seu PONTO (%d) de novo. Voce ganhou!\n", ponto);
                    saldo += aposta;
                    break;
                } 
                else if (soma == 7) {
                    printf("Voce tirou 7 antes do ponto. Voce perdeu!\n");
                    saldo -= aposta;
                    break;
                }
            }
        }

        printf("\nTotal em dinheiro: R$ %.2f\n", saldo);

        if (saldo <= 0) {
            printf("Voce ficou sem dinheiro! Fim de jogo.\n");
            break;
        }

        do {
            printf("Deseja continuar jogando? (1-Sim / 0-Nao): ");
            scanf("%d", &opcao);
            if (opcao != 0 && opcao != 1) {
                printf("Opcao invalida.\n");
            }
        } while (opcao != 0 && opcao != 1);

    } while (opcao == 1);

    printf("\nVoce saiu com: R$ %.2f\n", saldo);

    return 0;
}