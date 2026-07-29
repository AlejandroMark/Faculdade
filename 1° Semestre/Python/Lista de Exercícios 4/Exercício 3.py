'''
Dado dois números inteiros positivos, determinar o máximo divisor comum entre eles.
'''

num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))

if num1 < num2:
    menor = num1
else:
    menor = num2

while menor < 0:
    if num1 % menor == 0 and num2 % menor == 0:
        print("O MDC é de %d" %menor)
        break;
    menor -=1
