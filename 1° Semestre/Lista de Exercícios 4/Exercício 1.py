'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Atenção: só existe fatorial de números maiores que zero.
'''

numero = int(input("Informe um número: "))

while numero <= 0:
    print("Número inválido! Digite maior que zero.")
    numero = int(input("Informe um número: "))

fatorial = 1

while numero > 1:
    fatorial = fatorial * numero
    numero = numero - 1

print("Fatorial: %d" %fatorial)