#Faça um Programa que leia três números e mostre o maior, o menor e mostre‐os em ordem decrescente.

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print("O maior numero é o primeiro %.2f" %(num1))
elif num2 > num1 and num2 > num3:
    print("O maior numero é o segundo %.2f" %(num2))
elif num3 > num1 and num3 > num2:
    print("O maior numero é o terceiro %.2f" %(num3))
else:
    print("Inválido")

if num1 < num2 and num1 < num3:
    print("O menor numero é o primeiro %.2f" %(num1))
elif num2 < num1 and num2 < num3:
    print("O menor numero é o segundo %.2f" %(num2))
elif num3 < num1 and num3 < num2:
    print("O menor numero é o terceiro %.2f" %(num3))
else:
    print("Inválido")
    
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)

elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)

else:
    if num1 >= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)