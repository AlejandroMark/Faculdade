# Calcular o fatorial de um número

num = int (input ("Digite um número: ") ) 
fat = 1
cont = 1
while cont <= num :
    fat = fat * cont
    cont = cont + 1

print ("O fatorial de %d é %d"  %(num, fat) )