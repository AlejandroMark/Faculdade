# Leia o preço de um produto e a quantidade vendida.
# Calcule o valor total da compra. 
# Até R$ 100,00 conceder desconto de 3%. 
# Até R$ 200,00 conceder um desconto de 5%.
# Até R$ 300,00 conceder desconto de 10%
# Acima de 300,00 conceder desconto de 15%

preco = float ( input("Preço: " )  ) 
qtde = int ( input("Quantidade: " )  )
total = preco * qtde
desconto = 0

if total <= 100 :
    porc = 3
elif total <= 200 :
    porc = 5
elif total <= 300:
    porc = 10
else:
    porc = 15
    
desconto = total * (porc/100)
totalAPagar = total - desconto

print("Você teve %d %% de desconto" %porc)
print ("Valor total: \t R$ %8.2f " %total)
print ("Desconto: \t R$ %8.2f " %desconto)
print("-" * 40)
print("Total a pagar: \t R$ %8.2f" %totalAPagar )