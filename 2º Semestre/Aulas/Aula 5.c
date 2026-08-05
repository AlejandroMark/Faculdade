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
    char letra;

    printf("1 - Inserir\n");
    printf("2 - Pesquisar\n");
    printf("3 - Alterar\n");
    printf("4 - Excluir\n");

    printf("Escolha a opção: ");
    scanf("%d", &opcao);
    
    switch ( opcao ) {
        case 1:
            printf("INSERIR. \n");    
            break;


        case 2:
            printf("PESQUISAR. \n");
            break;

        case 3:
            printf("ALTERAR. \n");
            break;

        case 4: case 5:
            printf("EXCLUIR. \n");
            break;

        default:
            printf("OPÇÃO INVÁLIDA!");
    }
    printf("E - Estudantil\n");
    printf("I - Internacional\n");
    printf("B - Black\n");
    printf("P - Platinum\n");

    printf("Escolha o tipo do seu cartão: ");
    scanf(" %c", &letra);

    switch ( letra ) {
        case 'E': case 'e':
            printf("ESTUDANTIL. \n");
            break;
        
        case 'I': case 'i':
            printf("INTERNACIONAL. \n");
            break;
        
        case 'B': case 'b':
            printf("BLACK. \n");
            break;
        
        case 'P': case 'p':
            printf("PLATINUM. \n");
            break;
        
        default:
            printf("OPÇÃO INVÁLIDA! \n");
            break;
    }
}