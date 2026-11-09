#include <stdio.h>
#include <stdlib.h>

FILE * abrirArquivo(char * nome, char * modo) {
    FILE * arquivo;
    arquivo = fopen(nome, modo);
    if (arquivo == NULL) {
        printf("ERRO ao abrir arquivo");
        exit(1);
    }
    return arquivo;
}

int main() {
    FILE * arqProd;
    FILE * arqVendas;
    FILE * arqSaida;
    int m1, m2;
    float custoM1, lucroM1, custoM2, lucroM2;
    float custoMes, lucroMes, receitaMes;
    float custoAno = 0.0, lucroAno = 0.0, receitaAno = 0.0;

    arqProd = abrirArquivo("ex2_producao.txt", "r");
    arqVendas = abrirArquivo("ex2_vendas.txt", "r");
    arqSaida = abrirArquivo("ex2_saida.txt", "w");

    fscanf(arqVendas, "%f %f", &custoM1, &lucroM1);
    fscanf(arqVendas, "%f %f", &custoM2, &lucroM2);

    while (!feof(arqProd)) {
        if (fscanf(arqProd, "%d %d", &m1, &m2) == 2) {
            custoMes = (m1 * custoM1) + (m2 * custoM2);
            lucroMes = (m1 * lucroM1) + (m2 * lucroM2);
            receitaMes = lucroMes - custoMes;

            fprintf(arqSaida, "%.2f %.2f %.2f\n", custoMes, lucroMes, receitaMes);

            custoAno = custoAno + custoMes;
            lucroAno = lucroAno + lucroMes;
            receitaAno = receitaAno + receitaMes;
        }
    }

    fprintf(arqSaida, "TOTAL ANO: %.2f %.2f %.2f\n", custoAno, lucroAno, receitaAno);

    printf("Custo Total no Ano: %.2f\n", custoAno);
    printf("Lucro Total no Ano: %.2f\n", lucroAno);
    printf("Receita Total no Ano: %.2f\n", receitaAno);
    printf("FIM DO PROGRAMA.");

    fclose(arqProd);
    fclose(arqVendas);
    fclose(arqSaida);
    return 0;
}