'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber o valor de cada produto comprado. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e 
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o 
programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo, onde o preço de cada produto será digitado:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 8.00
Dinheiro: R$ 20.00
Troco: R$ 12.00
...
'''
print("Lojas Tabajara")

contador = 1
total = 0

while contador < 3:

    produto = float(input("Informe o valor do produto: "))
    if produto == 0:
        break
    total += produto
    contador += 1

print("Total: R$ %.2f" % total)
dinheiro = float(input("Dinheiro: R$ "))
troco = dinheiro - total
print("Troco: R$ %.2f" % troco)
