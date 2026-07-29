# Validação com STRINGS

entrega = input ("É para entregar (S/N) ? ")
entrega = entrega.upper()
while entrega != "S" and entrega != "N" :
    print ("Digite S para SIM ou N para NÃO") 
    entrega = input ("É para entregar (S/N) ? ")
    entrega = entrega.upper()

print ("Você escolheu: %s" %entrega)