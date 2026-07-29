'''
Altere os exercícios 3, 4, 5, 6 e 8 da Lista 3 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 5 ####

def lerNome():
    nome = input("Informe o nome: ")
    return nome

def lerAltura():
    altura = float(input("Informe a altura: "))
    return altura

contador = 1
soma = 0

while contador <= 20:
    nome = lerNome()
    altura = lerAltura()

    soma += altura

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

print("\nAltura média: %.2f" %media)
print("Menor altura: %.2f - Menor nome: %s" %(menorAltura, nomeMenor))
print("Maior altura: %.2f - Maior nome: %s" %(maiorAltura, nomeMaior))