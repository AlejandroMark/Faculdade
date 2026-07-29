#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

numero = 2 ** 1000000

quantidade = len(str(numero))

print("A quantidade de dígitos em 2 elevado a um milhão é %d" %(quantidade))