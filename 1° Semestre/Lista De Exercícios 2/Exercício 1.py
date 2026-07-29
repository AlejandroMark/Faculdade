#1. Faça um Programa que peça dois números e imprima o maior deles. 

a = float(input("Número a: "))
b = float(input("Numero b: "))

if a > b:
    print("O numero maior é A %.2f" %(a))
else:
    print("O numero maior é B %.2f" %(b))