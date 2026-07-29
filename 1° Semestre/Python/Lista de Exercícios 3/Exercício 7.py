'''
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A ultrapasse ou 
iguale a população do país B, mantidas as taxas de crescimento.
'''

A = 8000
B = 200000
AC = 3
BC = 1.5

while A < B:
    anos = int(input("Informe a quantidade de anos: "))
    AnosA = A + (3 * anos)
    AnosB = B + (1.5 * anos)

    print("Anos A: %.2f" %AnosA)
    print("Anos B: %.2f" %AnosB)

    if A < B:
        print("A será maior em %d anos" %anos)
        A = AnosA
        B = AnosB
    else:
        print("A ainda não é maior")