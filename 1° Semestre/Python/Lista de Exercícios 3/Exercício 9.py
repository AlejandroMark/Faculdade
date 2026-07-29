'''
Anacleto tem 1,50 m e cresce 2 cm por ano, enquanto 
Felisberto tem 1,10 m e cresce 3 cm por ano. Construa 
um programa que calcule e imprima quantos anos serão 
necessários para que Felisberto seja maior que Anacleto.
'''

Anacleto = 1.50
Felisberto = 1.10

while Felisberto < Anacleto:
    anos = int(input("Informe quantos anos: "))
    alturaAnacleto = Anacleto + (0.02 * anos)
    alturaFelisberto = Felisberto + (0.03 * anos)

    print("Altura do Anacleto: %.2f" %alturaAnacleto)
    print("Altura do Felisberto: %.2f" %alturaFelisberto)

    if alturaFelisberto > alturaAnacleto:
        print("Felisberto será maior em %d anos" %anos)
        Felisberto = alturaFelisberto
        Anacleto = alturaAnacleto
    else:
        print("Felisberto ainda não será maior")