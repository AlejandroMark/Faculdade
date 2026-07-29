#2. Faça um programa que peça o nome do aluno e suas 4 notas bimestrais e mostre o nome do aluno e a média.

nome = str(input("Informe o nome do aluno: "))
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta nota: "))

media = (n1 + n2 + n3 + n4) /4

print("A media do aluno é %.2f" %(media))