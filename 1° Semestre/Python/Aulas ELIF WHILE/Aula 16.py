# Calcular o total das vendas de um dia
# Parar quando digitar um valor negativo

total = 0
cont = 0
venda = float (input ("Valor da venda: ") ) 
while venda > 0 :
    total = total + venda
    cont = cont + 1

    # Ler a próxima venda
    venda = float (input ("Valor da venda: ") ) 

print ("Foram realizadas %d vendas."  %cont )
print ("O valor total vendido foi de R$ %.2f"  %total )