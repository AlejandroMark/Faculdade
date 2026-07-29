'''
Uma Empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores de consumo. Para cada consumidor, são digitados os seguintes dados:
- Número do consumidor;
- Quantidade de kWh consumidos durante o mês;
- Tipo (código) do consumidor:
1 - residencial, preço em reais por kWh = 0,3
2 - comercial, preço em reais por kWh = 0,5
3 - industrial, preço em reais por kWh = 0,7
Os dados devem ser lidos até que seja encontrado um consumidor com Número 0 (zero). Escreva um programa que calcule e imprima:
a) O custo total para cada consumidor;
b) O total de consumo para cada um dos três tipos de consumidor;
c) A média de consumo dos tipos 1 e 2.
'''

rekw = 0.3
cokw = 0.5
inkw = 0.7

total1 = 0
total2 = 0
total3 = 0

qtd1 = 0
qtd2 = 0

nCON = int(input("Número do consumidor: "))

while nCON != 0:

    kwh = float(input("kWh consumido por mês: "))
    tCOD = int(input("Código do consumidor: "))

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

    print("Custo total: R$%.2f" %custo)

    nCON = int(input("\nNúmero do consumidor: "))

media1 = total1 / qtd1
media2 = total2 / qtd2

print("\nTotal consumido residencial:" %total1)
print("Total consumido comercial:" %total2)
print("Total consumido industrial:" %total3)

print("Média consumo tipo 1:" %media1)
print("Média consumo tipo 2:" %media2)