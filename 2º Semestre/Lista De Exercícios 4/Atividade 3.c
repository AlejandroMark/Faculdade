/*  O programa abaixo calcula a área das figuras geométricas retângulo e círculo. Implemente as
funções que estão faltando e complete o programa principal abaixo para que ele execute
corretamente.
 A área do retângulo é: base * altura
 A área do círculo é: PI * raio2
(Para pegar o valor de PI, use: M_PI)
 O tamanho de cada informação (base, altura e raio) deve ser maior que zero.
 A opção a ser lida deve ser 0, 1 e 2. */

#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h> // Para pegar o PI

int lerOpcao()
{
    int op;
    do {
        printf("\n\nCALCULAR A AREA:\n");
        printf("1-Retangulo\n");
        printf("2-Circulo\n");
        printf("0-Sair\n");
        printf("Informe sua opcao: ");
        scanf("%d", &op);
        
        if (op < 0 || op > 2) {
            printf("Opcao invalida! Digite 0, 1 ou 2.\n");
        }
    } while (op < 0 || op > 2);

    return op;
}

float calcularAreaRetangulo(float base, float altura)
{
    return base * altura;
}

float calcularAreaCirculo(float raio)
{
    return M_PI * raio * raio;
}

int main()
{
    int opcao;
    float base, altura, raio, area;

    do
    {
        opcao = lerOpcao();
        switch (opcao)
        {
        case 1:
            printf("\n\tAREA DO RETANGULO\n");
            
            do {
                printf("Digite a base: ");
                scanf("%f", &base);
                if (base <= 0) printf("A base deve ser maior que zero.\n");
            } while (base <= 0);

            do {
                printf("Digite a altura: ");
                scanf("%f", &altura);
                if (altura <= 0) printf("A altura deve ser maior que zero.\n");
            } while (altura <= 0);

            area = calcularAreaRetangulo(base, altura);
            printf("Area do Retangulo: %.2f\n", area);
            break;

        case 2:
            printf("\n\tAREA DO CIRCULO\n");
            
            do {
                printf("Digite o raio: ");
                scanf("%f", &raio);
                if (raio <= 0) printf("O raio deve ser maior que zero.\n");
            } while (raio <= 0);

            area = calcularAreaCirculo(raio);
            printf("Area do Circulo: %.2f\n", area);
            break;
        }
    } while (opcao > 0);

    return 0;
}