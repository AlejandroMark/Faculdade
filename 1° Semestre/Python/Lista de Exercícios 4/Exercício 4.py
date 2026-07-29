'''
A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.
Faça um algoritmo que leia um número inteiro e calcule a sequência de Fibonacci. 
Por exemplo, se o usuário informar o número 10, então mostrar os 10 primeiros números da sequência.
'''

n = int(input("Quantos números você quer ver? "))

a = 1
b = 1
contador = 0

while contador < n:
    print(a, b)

    novo = a + b
    a = b
    b = novo
    contador += 1