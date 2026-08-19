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
    printf("\n\nCALCULAR A ÁREA:\n");
    printf("1-Retângulo\n");
    printf("2-Círculo\n");
    printf("0-Sair\n");
    printf("Informe sua opção: ");
    scanf("%d", &op);
    // VALIDAR a opção entre 0, 1 e 2
    return op;
}
int main()
{
    int opcao;
    do
    {
        opcao = lerOpcao();
        switch (opcao)
        {
        case 1:
            printf("\n\tÁREA DO RETÂNGULO\n");
            // Ler os dados para calcular a área do RETANGULO
            // Chamar a função para calcular a área do RETANGULO
            // Mostrar o resultado
            break;
        case 2:
            printf("\n\tÁREA DO CÍRCULO\n");
            // Ler os dados para calcular a área do CIRCULO
            // Chamar a função para calcular a área do CIRCULO
            // Mostrar o resultado
            break;
        }
    } while (opcao > 0);
    return 0;
}
