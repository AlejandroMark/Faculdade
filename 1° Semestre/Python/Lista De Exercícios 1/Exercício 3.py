#3. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Informe os dias: "))
horas = int(input("Informe as horas: "))
min = int(input("Informe os minutos: "))
seg = int(input("Informe os segundos: "))

Dias = dias*24*60*60
print("Dias para horas é %d" %(Dias))

Horas = horas*60*60
print("Horas para minutos é %d" %(Horas))

Min = min*60
print("Minutos para segundos é %d " %(Min))

Seg = seg
print("Segundos %d" %(Seg))