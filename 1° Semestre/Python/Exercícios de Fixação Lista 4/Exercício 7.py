'''
Altere os exercícios 1, 2, 3, 4, 6, 7 e 8 da Lista 4 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 8 ####

def lerNumeroConsumidor():
    nCON = int(input("Número do consumidor: "))
    return nCON

def lerKwh():
    kwh = float(input("kWh consumido por mês: "))
    return kwh

def lerCodigoTipo():
    tCOD = int(input("Código do consumidor: "))
    return tCOD

rekw = 0.3
cokw = 0.5
inkw = 0.7

total1 = 0
total2 = 0
total3 = 0

qtd1 = 0
qtd2 = 0

nCON = lerNumeroConsumidor()

while nCON != 0:
    kwh = lerKwh()
    tCOD = lerCodigoTipo()

    if tCOD == 1:
        custo = kwh * rekw
        total1 += kwh
        qtd1 += 1
    elif tCOD == 2:
        custo = kwh * cokw
        total2 += kwh
        qtd2 += 1
    elif tCOD == 3:
        custo = kwh * inkw
        total3 += kwh

    print("Custo total: R$%.2f" % custo)
    nCON = lerNumeroConsumidor()

media1 = total1 / qtd1
media2 = total2 / qtd2

print("\nTotal consumido residencial: %f" % total1)
print("Total consumido comercial: %f" % total2)
print("Total consumido industrial: %f" % total3)

print("Média consumo tipo 1: %f" % media1)
print("Média consumo tipo 2: %f" % media2)