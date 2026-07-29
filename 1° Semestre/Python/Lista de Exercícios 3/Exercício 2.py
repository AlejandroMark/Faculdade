'''
Altere o programa anterior para ler o nome do aluno e suas três notas. Valide a entrada das notas. 
Calcule a média final do aluno e imprima: “APROVADO” se a média for maior ou igual a 7; “REPROVADO” se a média for menor 
que 6; e “PROVA FINAL” se a média estiver entre 6 e 7. Imprima também as notas na ordem decrescente.
'''

nome = input("Nome do aluno: ")

nota1 = float(input("1° nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida! Digite novamente: "))

nota2 = float(input("2° nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida! Digite novamente: "))
    
nota3 = float(input("3° nota: "))
while nota3 < 0 or nota3 > 10:
    nota3 = float(input("Nota inválida! Digite novamente: "))

media = (nota1 + nota2 + nota3) / 3

print("Média: %.2f" %media)

if nota1 >= nota2 and nota1 >= nota3:
    maior = nota1
    if nota2 >= nota3:
        meio = nota2
        menor = nota3
    else:
        meio = nota3
        menor = nota2

elif nota2 >= nota1 and nota2 >= nota3:
    maior = nota2
    if nota1 >= nota3:
        meio = nota1
        menor = nota3
    else:
        meio = nota3
        menor = nota1

else:
    maior = nota3
    if nota1 >= nota2:
        meio = nota1
        menor = nota2
    else:
        meio = nota2
        menor = nota1

print("Notas em ordem decrescente: %.2f, %.2f, %.2f" %(maior, meio, menor))

if media >= 7:
    print("APROVADO")
elif media < 6:
    print("REPROVADO")
else:
    print("PROVA FINAL")