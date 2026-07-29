#5. Solicite o nome, a quantidade e o preço de um produto e o percentual de desconto. Exiba o nome do produto, o valor do desconto e o preço a pagar.

nomeProduto = str(input("Informe o nome do produto: "))
qtdProduto = int(input("Informe a quantidade de produto: "))
precoProduto = float(input("Informe o preço do produto: "))
percentual = int(input("Informe o percentual de desconto do produto: "))

print("\n")

print("O nome do produto é %s" %(nomeProduto))

desconto = qtdProduto - (precoProduto/100)
print("O Valor de desconto do produto é de %d" %(desconto))

precoPagar = precoProduto + desconto
print("Preço a pagar do produto é de %f" %(precoPagar))