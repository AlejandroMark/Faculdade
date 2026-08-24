#include <stdio.h>

float lerPeso() {
    // Ler e validar o peso
    float peso;
	do {
		printf("\n\tInforme o PESO: ");
		scanf("%f", &peso);	
	} while ( peso <= 0 || peso >= 500 );

    return peso;

}


float lerAltura() {
    float altura;
    // Ler e validar a altura
    do {
        printf("\n\tInforme a ALTURA: ");
        scanf("%f", &altura);	
    } while ( altura <= 0.1 || altura >= 2.5 );

    return altura;
}


float lerIdade() {
    float id;
    // Ler e validar a idade
    do {
        printf("\n\tInforme a IDADE: ");
        scanf("%f", &id);	
    } while ( id < 0 || id >= 150 );

    return id;
}


void lerDadosCliente(float *peso, float *alt, int *idade) {
    *peso = lerPeso();
    *alt = lerAltura();
    *idade = lerIdade();
}


int main() { 
    float peso1, peso2, alt1, alt2;
    int idade1, idade2;

    // Ler dados CLIENTE 1
    lerDadosCliente(&peso1, &alt1, &idade1);
    

    // Ler dados CLIENTE 2
    lerDadosCliente(&peso2, &alt2, &idade2);
    


    // lerDadosFuncionario( ... )

    /// lerAcademicos( . . . )
 

    // Calcular IMC
    // imc (peso, alt);
    
    printf("\nCLIENTE 1: \n");
    printf("\tPeso: %.1f\tAltura: %.2f\tIdade: %d\n", peso1, alt1, idade1);

    printf("\nCLIENTE 2: \n");
    printf("\tPeso: %.1f\tAltura: %.2f\tIdade: %d\n", peso2, alt2, idade2);

    return 0;
}