/* Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais
baixo, o mais gordo e o mais magro. Para isto você deve fazer um programa que pergunte a
cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de
dados deve ser dado quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa devem ser informados os códigos e valores do cliente mais alto, do mais baixo, do
mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
*/

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// PRINCIPAL
int main() 
{
    // Para acentuação
    SetConsoleOutputCP(65001);

    int codigo;
    float altura, peso;

    int mAlto, mBaixo, mGordo, mMagro;

    float mais_alto, mais_baixo, mais_gordo, mais_magro;

    float soma_alturas = 0, soma_pesos = 0;
    int total_clientes = 0;

    while (1) 
    {
        printf("Informe o código do cliente (ou 0 para encerrar): ");
        scanf("%d", &codigo);

        if (codigo == 0) {
            break;
        }

        do {
            printf("Informe a altura (em metros): ");
            scanf("%f", &altura);
            if (altura <= 0) {
                printf("Altura inválida! Digite um valor positivo.\n");
            }
        } while (altura <= 0);

        do {
            printf("Informe o peso (em kg): ");
            scanf("%f", &peso);
            if (peso <= 0) {
                printf("Peso inválido! Digite um valor positivo.\n");
            }
        } while (peso <= 0);

        soma_alturas += altura;
        soma_pesos += peso;
        total_clientes++;

        if (total_clientes == 1) 
        {
            mais_alto = altura;
            mAlto = codigo;

            mais_baixo = altura;
            mBaixo = codigo;

            mais_gordo = peso;
            mGordo = codigo;

            mais_magro = peso;
            mMagro = codigo;
        } 
        else 
        {
            if (altura > mais_alto) {
                mais_alto = altura;
                mAlto = codigo;
            }
            if (altura < mais_baixo) {
                mais_baixo = altura;
                mBaixo = codigo;
            }

            if (peso > mais_gordo) {
                mais_gordo = peso;
                mGordo = codigo;
            }
            if (peso < mais_magro) {
                mais_magro = peso;
                mMagro = codigo;
            }
        }

        printf("\n--- Cliente cadastrado com sucesso! ---\n\n");
    }

    if (total_clientes > 0) 
    {
        printf("\n================ RESULTADO DO CENSO ================\n");
        printf("Cliente Mais Alto  : Código %d | Altura: %.2fm\n", mAlto, mais_alto);
        printf("Cliente Mais Baixo : Código %d | Altura: %.2fm\n", mBaixo, mais_baixo);
        printf("Cliente Mais Gordo : Código %d | Peso: %.2fkg\n", mGordo, mais_gordo);
        printf("Cliente Mais Magro : Código %d | Peso: %.2fkg\n", mMagro, mais_magro);
        printf("----------------------------------------------------\n");
        printf("Média de Altura dos Clientes : %.2fm\n", soma_alturas / total_clientes);
        printf("Média de Peso dos Clientes   : %.2fkg\n", soma_pesos / total_clientes);
        printf("====================================================\n");
    } 
    else 
    {
        printf("\nNenhum cliente foi cadastrado.\n");
    }

    return 0;
}