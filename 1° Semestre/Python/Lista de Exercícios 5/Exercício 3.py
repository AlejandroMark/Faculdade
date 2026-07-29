'''
Faça um programa para imprimir:
 1
 2 2
 3 3 3
 .....
 n n n n n n ... n
para um n informado pelo usuário. Use uma função para ler e validar o valor n (inteiro e
positivo) e outra função para imprimir até a n-ésima linha.
'''

def lerNumeroInt():
    num = input("Número inteiro: ")
    while num.isdigit() == False:
        print("Número inteiro inválido!")
        num = input("Número inteiro: ") 
    return int(num)

def lerNumero():
    num = lerNumeroInt() 
    while num <= 0:
        print("Número Inválido! ")
        num = lerNumeroInt()
    return num

def mostrarUMAlinha(num):
    cont = 1
    while cont <= num:
        print(num, end=" ")
        cont = cont + 1

def calcular(n):
    cont = 1
    while cont <= n:
        mostrarUMAlinha(cont)
        print()
        cont = cont + 1

### Programa Principal ###
def main():
    n = lerNumero()
    calcular(n)

main()