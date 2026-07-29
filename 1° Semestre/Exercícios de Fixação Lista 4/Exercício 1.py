'''
Altere os exercícios 1, 2, 3, 4, 6, 7 e 8 da Lista 4 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 1 ####

def lerNumero():
    numero = int(input("Informe um número maior que zero: "))
    return numero

# Leitura inicial
numero = lerNumero()

# Validação do dado
while numero <= 0:
    print("Número inválido!")
    numero = lerNumero()

# Cálculo do fatorial
fatorial = 1
temp_numero = numero
while temp_numero > 1:
    fatorial *= temp_numero
    temp_numero -= 1

print("O fatorial de %d é: %d" % (numero, fatorial))