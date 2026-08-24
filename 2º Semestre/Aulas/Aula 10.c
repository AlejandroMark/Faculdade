#include <stdio.h>

void trocar (int *n1, int *n2) {
    int aux;
    aux = *n1;
    *n1 = *n2;
    *n2 = aux;
}

int main() {
    int a, b;
    // a = 10;
    // b = 20;        

    printf("Número 1: ");    
    scanf("%d", &a);

    printf("Número 2: ");
    scanf("%d", &b);


    printf("\n\tANTES: a= %d\tb= %d\n\n", a, b);
    
    trocar(&a, &b);
    
    printf("\n\tDEPOIS: a= %d\tb= %d\n\n", a, b);
    return 0;
}