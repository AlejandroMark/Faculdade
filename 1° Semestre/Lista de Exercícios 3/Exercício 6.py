'''
Faça um programa para ler vários números positivos entre 1 e 1000, 
validar e só parar quando o usuário digitar -1. 

No final imprima:
- o maior número
- a quantidade de números pares
- a quantidade de números ímpares
- a média dos números pares
- a média dos números ímpares
- a soma total de todos os números lidos
'''

contadorPar = 0
contadorImpar = 0
somaPar = 0
somaImpar = 0
somaTotal = 0
maior = 0

numero = int(input("Informe um número: "))

while numero != -1:

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