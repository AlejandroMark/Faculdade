'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1. 
Caso o número não seja primo, por quais números ele é divisível.
'''

numero = int(input("Informe um numero: ")) 

divisor = 2
primo = True
if numero <= 1:
    primo = False

while divisor < numero:
    if numero % divisor == 0:
        primo = False
    
    divisor += 1
if primo:
    print("O número %d é primo " %numero)
else:
    print("O número %d não é primo " %numero)