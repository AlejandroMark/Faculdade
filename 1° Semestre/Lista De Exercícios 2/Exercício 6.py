''' Um posto está vendendo combustíveis com a seguinte tabela de descontos: 

Álcool: a. até 20 litros, desconto de 3% por litro. b. acima de 20 litros, desconto de 5% por litro. 
Gasolina: a. até 20 litros, desconto de 4% por litro. b. acima de 20 litros, desconto de 6% por litro. 

Escreva um programa que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor aser pagopelo cliente sabendo-se que 
o preço do litro da gasolina é R$ 3,90 e o preçodolitrodoálcool é R$ 3,20 
'''

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A/G): ")

PA = 3.20
PG = 3.90

if tipo == "A" or tipo == "a":
    valor = litros * PA
    if litros <= 20:
        desconto = valor * 0.03
    else:
        desconto = valor * 0.05
    total = valor - desconto
    print("Valor a pagar: R$ %.2f" %(total))
elif tipo == "G" or tipo == "g":
    valor = litros * PG
    if litros <= 20:
        desconto = valor * 0.04
    else:
        desconto = valor * 0.06
    total = valor - desconto
    print("Valor a pagar: R$ %.2f" % total)
else:
    print("Tipo de combustível inválido!")