#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int opcao;

    printf("1 - Inserir\n");
    printf("2 - Pesquisar\n");
    printf("3 - Alterar\n");
    printf("4 - Excluir\n");

    printf("Escolha a opção: ");
    scanf("%d", &opcao);

    if ( opcao == 1) {
        printf("INSERIR \n");
    } 
    else if ( opcao == 2) {
        printf("PESQUISAR \n");
    } 
    else if ( opcao == 3) {
        printf("ALTERAR \n");
    } 
    else if (opcao == 4){
        printf("EXCLUIR \n");
    } 
    else {
        printf("OPÇÃO INVÁLIDA! \n");
    }
}