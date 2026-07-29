# Imprima os números pares até um valor digitado

num = int(input("Digite um número: ") )
x = 0
while x <= num :
    if (x % 2) == 0 :
        print ("%4d" %x, end="")
    x = x + 1