'''
Altere os exercícios 3, 4, 5, 6 e 8 da Lista 3 para usar funções.
Coloque apenas as funções para ler as informações.
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 6 ####

contadorPar = 0
contadorImpar = 0
somaPar = 0
somaImpar = 0
somaTotal = 0
maior = 0

def lerNumero():
    numero = int(input("Informe um número: "))
    return numero

while numero != -1:
    numero = lerNumero()
    if numero < 1 or numero > 1000:
        print("Número inválido!")
    else:
        somaTotal = somaTotal + numero
        if numero > maior:
            maior = numero
        if numero % 2 == 0:
            contadorPar += 1
            somaPar = somaPar + numero
        else:
            contadorImpar += 1
            somaImpar = somaImpar + numero

numero = int(input("Informe um número: "))

if contadorPar > 0:
    mediaPar = somaPar / contadorPar
else:
    mediaPar = 0
    
if contadorImpar > 0:
    mediaImpar = somaImpar / contadorImpar
else:
    mediaImpar = 0

print("Maior número: %.2f" %maior)
print("Quantidade de pares: %.2f" %contadorPar)
print("Quantidade de ímpares: %.2f" %contadorImpar)
print("Média dos pares: %.2f" %mediaPar)
print("Média dos ímpares: %.2f" %mediaImpar)
print("Soma total: %.2f" %somaTotal)