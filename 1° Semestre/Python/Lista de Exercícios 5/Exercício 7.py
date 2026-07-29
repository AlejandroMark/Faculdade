'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por
exemplo, o programa deve converter 14:25 em 2:25 P.M (outro exemplo: 9:45 converte em
9:45 A.M.). A entrada é dada em dois inteiros, um para a hora e outro para os minutos.
Usar função para ler cada número e validar. Criar outra função para fazer a conversão.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de
entrada todas as vezes que desejar. 
'''

def lerHora():
    hora = int(input("Informe a hora: "))

    while hora < 0 or hora > 23:
        print("Hora inválida!")
        hora = int(input("Informe a hora: "))

    return hora


def lerMinuto():
    minuto = int(input("Informe os minutos: "))

    while minuto < 0 or minuto > 59:
        print("Minuto inválido!")
        minuto = int(input("Informe os minutos: "))

    return minuto


def converterHora(hora, minuto):
    if hora == 0:
        print("12:", minuto, "A.M.")
    elif hora < 12:
        print(hora, ":", minuto, "A.M.")
    elif hora == 12:
        print("12:", minuto, "P.M.")
    else:
        print(hora - 12, ":", minuto, "P.M.")


continuar = "S"

while continuar == "S":
    hora = lerHora()
    minuto = lerMinuto()

    converterHora(hora, minuto)

    continuar = input("Deseja continuar? (S/N): ").upper()