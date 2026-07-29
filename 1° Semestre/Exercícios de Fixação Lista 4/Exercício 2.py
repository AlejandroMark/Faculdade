'''
Altere os exercícios 1, 2, 3, 4, 6, 7 e 8 da Lista 4 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 2 ####

def lerNumero():
    # Solicita o número ao usuário
    numero = int(input("Informe um numero: ")) 
    return numero 

# Lê o valor
numero = lerNumero()

divisor = 2
primo = True

# Verifica se o número não é primo
if numero <= 1:
    primo = False

# Loop de verificação de divisibilidade
while divisor < numero:
    if numero % divisor == 0:
        primo = False 
    divisor += 1

# Exibe o resultado
if primo:
    print("O número %d é primo " %numero)
else:
    print("O número %d não é primo " %numero)