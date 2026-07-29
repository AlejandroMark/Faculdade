# Leia o preço de um produto e a quantidade vendida.
# Calcule o valor total da compra. 
# Até R$ 100,00 conceder desconto de 3%. 
# Acima de R$ 100,00, então conceder um desconto de 5%.

preco = float ( input("Preço: " )  ) 
qtde = int ( input("Quantidade: " )  )
total = preco * qtde

if total <= 100 :
    porc = 3
else:
    porc = 5
    
desconto = total * (porc/100)
totalAPagar = total - desconto

print("Você teve %d %% de desconto" %porc)
print ("Valor total: \t R$ %8.2f " %total)
print ("Desconto: \t R$ %8.2f " %desconto)
print("-" * 40)
print("Total a pagar: \t R$ %8.2f" %totalAPagar )