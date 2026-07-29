'''
Altere o programa anterior permitindo ao usuário informar as 
populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
'''

continuar = "s"

while continuar == "s":

    A = int(input("Informe a população da cidade A: "))
    B = int(input("Informe a população da cidade B: "))

    AC = float(input("Informe a taxa de crescimento de A: "))
    BC = float(input("Informe a taxa de crescimento de B: "))
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
            
        print("A será maior que B em %d anos" %anos)
        print("População final de A: %.2f" %A)
        print("População final de B: %.2f" %B)

    continuar = input("Deseja repetir? [s/n]: ")