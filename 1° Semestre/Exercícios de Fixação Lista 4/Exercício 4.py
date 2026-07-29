'''
Altere os exercícios 1, 2, 3, 4, 6, 7 e 8 da Lista 4 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 4 ####

def lerNumero():
    # Solicita a quantidade de números
    numero = int(input("Quantos números da sequência deseja ver? "))
    return numero

# Chama a função
numero = lerNumero()

a = 1
b = 1
contador = 0

# Loop para calcular e mostrar a sequência
while contador < numero:
    print(a)
    # Calcula o próximo número
    novo = a + b
    a = b
    b = novo
    contador += 1