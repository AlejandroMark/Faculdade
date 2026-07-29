'''
Altere os exercícios 3, 4, 5, 6 e 8 da Lista 3 para usar funções.
Coloque apenas as funções para ler as informações.
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCÍCIO 8 ####

continuar = "s"

def lerA():
    A = int(input("Informe a população da cidade A: "))
    return A

def lerB():
    B = int(input("Informe a população da cidade B: "))
    return B

def lerAC():
    AC = float(input("Informe a taxa de crescimento de A: "))
    return AC

def lerBC():
    BC = float(input("Informe a taxa de crescimento de B: "))
    return BC

while continuar == "s":

    A = lerA()
    B = lerB()

    AC = lerAC()
    BC = lerBC()

    if A <= 0 or B <= 0:
        print("População inválida!")

    elif AC <= 0 or BC <= 0:
        print("Taxa inválida!")

    else:
        anos = 0

        while A < B:
            A = A + (A * (AC / 100))
            B = B + (B * (BC / 100))
            anos += 1

        print("A será maior que B em %d anos" % anos)
        print("População final de A: %.2f" % A)
        print("População final de B: %.2f" % B)

    continuar = input("Deseja repetir? [s/n]: ").lower()