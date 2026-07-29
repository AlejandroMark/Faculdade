# Leia o preço de um produto e a quantidade vendida
# e calcule o valor total da compra.
# Se for maior que R$ 100,00, então conceder um desconto de 5%.


# Ler e validar o preco
preco = float(input("Informe o preço do produto: ") )
while preco <= 0 :
    print("Preço inválido!")
    preco = float(input("Informe o preço do produto: ") )     


# Ler e validar a quantidade
qtde = int(input("Informe a quantidade vendida: ") )
while qtde <= 0 :
    print("Qtde inválida!")
    qtde = int(input("Informe a quantidade vendida: ") )

total = preco * qtde

if total > 100 :
    desconto = total * (5/100)
    total = total - desconto
    
print("O total a pagar é R$ %.2f"  %total) 