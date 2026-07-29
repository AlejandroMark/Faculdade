# Leia o preço de um produto e a quantidade vendida.
# Calcule o valor total da compra. 
# Se for maior que R$ 100,00, então conceder um desconto de 5%.

preco = float ( input("Preço: " )  ) 
qtde = int ( input("Quantidade: " )  )
total = preco * qtde
desconto = 0

if total > 100 :
    desconto = total * (5/100)
       
totalAPagar = total - desconto

print ("Valor total: \t R$ %8.2f " %total)
print ("Desconto: \t R$ %8.2f " %desconto)
print("-" * 40)
print("Total a pagar: \t R$ %8.2f" %totalAPagar )