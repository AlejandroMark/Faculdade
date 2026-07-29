preco = float(input("Preço do produto: "))
qtde = int(input("Quantidade: "))

total = preco * qtde
print("TOTAL: R$ %.2f" % total)

if total <= 100:
    porc = 3
elif total <= 200:
    porc = 5
elif total <= 300:
    porc = 10
else:
    porc = 15

desconto = (porc / 100) * total
total = total - desconto

print("Desconto (%d%%): R$ %.2f" % (porc, desconto))
print("A pagar: R$ %.2f" % total)