'''
Altere os exercícios 1, 2, 3, 4, 6, 7 e 8 da Lista 4 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 3 ####

def lerNumero():
    numero = int(input("Informe um número inteiro positivo: "))
    return numero

# Leitura usando a função
num1 = lerNumero()
num2 = lerNumero()

# Define o menor número para começar a busca do MDC
if num1 < num2:
    menor = num1
else:
    menor = num2

# O while deve rodar enquanto 'menor' for maior que 0
while menor > 0:
    if num1 % menor == 0 and num2 % menor == 0:
        print("O MDC é %d" % menor)
        break
    menor -= 1