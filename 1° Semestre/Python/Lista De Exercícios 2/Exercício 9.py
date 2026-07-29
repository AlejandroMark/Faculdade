'''
Faça um programa que receba o código e a quantidade de um produto comprado. Calcule e mostre: 
O preço unitário do produto comprado, conforme Tabela 1; 
O valor total da nota; 
O valor de desconto, conforme Tabela 2, e aplicado sobre o valor total; 
O valor total depois do desconto.
'''

'''
Faça um programa que receba o código e a quantidade de um produto comprado.
Calcule e mostre:
- O preço unitário
- O valor total
- O valor do desconto
- O valor total depois do desconto
'''

codP = int(input("Informe o codigo do produto: "))
quaP = int(input("Informe a quantidade do produto: "))

if codP >= 1 and codP <= 10:
    preco = 10

elif codP >= 11 and codP <= 20:
    preco = 15

elif codP >= 21 and codP <= 30:
    preco = 20

elif codP >= 31 and codP <= 40:
    preco = 30

else:
    print("Invalido")
print("Preço unitario: R$ %.2f" % preco)

total = quaP * preco
print("Valor total: R$ %.2f" % total)

if total <= 250:
    desconto = total * (5/100)

elif total > 250 and total <= 500:
    desconto = total * (10/100)

else:
    desconto = total * (15/100)
print("Valor do desconto: R$ %.2f" % desconto)

final = total - desconto
print("Valor final com desconto: R$ %.2f" % final)