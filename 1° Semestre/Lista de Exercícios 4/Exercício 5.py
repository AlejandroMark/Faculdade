'''
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém a quantidade de itens e o valor total, 
já que todos os itens custam R$ 1,99. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 itens, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
Preço unitário: R$ 1,99
QTDE TOTAL
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
'''

itens = 1.99
contador = 1

while contador <= 50:
    total = itens * contador
    print("O preço fica: %.2f " %total)
    contador += 1