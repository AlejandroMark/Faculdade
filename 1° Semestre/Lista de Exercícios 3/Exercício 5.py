'''
Desenvolver um programa que leia o nome e a altura de 20 pessoas.
Este programa deverá calcular e mostrar:
a) A altura média do grupo;
b) A menor altura do grupo e o nome da pessoa;
c) A maior altura do grupo e o nome da pessoa;
'''

contador = 1
soma = 0

while contador <= 3:
    nome = input("Informe o nome: ")
    altura = float(input("Informe a altura: "))
    soma = soma + altura
    if contador == 1:
        menorAltura = altura
        maiorAltura = altura
        nomeMenor = nome
        nomeMaior = nome
    if altura < menorAltura:
        menorAltura = altura
        nomeMenor = nome
    elif altura > maiorAltura:
        maiorAltura = altura
        nomeMaior = nome
    contador += 1
media = soma / 20

print(f"\nAltura média: {media:.2f}m")
print(f"Menor altura: {menorAltura:.2f}m - {nomeMenor}")
print(f"Maior altura: {maiorAltura:.2f}m - {nomeMaior}")