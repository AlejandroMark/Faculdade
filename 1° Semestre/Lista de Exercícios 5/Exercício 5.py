'''
O número de combinações possíveis de m elementos em grupos de n elementos (n <= m)
é dada pela fórmula de combinação m!/((m-n)!n!).
Escreva um programa que lê dois inteiros m e n e calcula a combinação de m, n a n.
Crie uma função para calcular o fatorial e chame essa função várias vezes.
'''

def lerNumero():
    numero = int(input("Informe um número: "))
    while numero < 0:
        print("Número inválido!")
        numero = int(input("Informe um número: "))
    return numero

def fatorial(num):
    fat = 1
    contador = 1
    while contador <= num:
        fat = fat * contador
        contador += 1
    return fat

def calcular(m, n):
    res = fatorial(m) / (fatorial(m - n) * fatorial(n))
    return res

def main():
    m = lerNumero()
    n = lerNumero()
    while n > m:
        print("n deve ser menor ou igual a m!")
        n = lerNumero()
    res = calcular(m, n)
    print("A combinação é: %.0f" % res)

main()