#4. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Informe o salario: "))
porc = float(input("Informe a porcentagem: "))

aumento = salario * (porc/100)
print("Aumento do salario foi de %f" %(aumento))

NSalario = salario + aumento
print("Novo salario é de %f" %(NSalario))