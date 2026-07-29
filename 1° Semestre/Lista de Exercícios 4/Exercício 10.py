'''
Altere o programa da questão anterior para que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''

maiorNota = -1
menorNota = 9999
totalAlunos = 0
somaNotas = 0
continuar = "S"

print("--- PROFESSOR: CADASTRO DO GABARITO ---")

gab1 = input("Gabarito 1: ").upper()
while (gab1 != "A") and (gab1 != "B") and (gab1 != "C") and (gab1 != "D") and (gab1 != "E"):
    print("Resposta Inválida!")
    gab1 = input("Gabarito 1: ").upper()

gab2 = input("Gabarito 2: ").upper()
while (gab2 != "A") and (gab2 != "B") and (gab2 != "C") and (gab2 != "D") and (gab2 != "E"):
    print("Resposta Inválida!")
    gab2 = input("Gabarito 2: ").upper()

gab3 = input("Gabarito 3: ").upper()
while (gab3 != "A") and (gab3 != "B") and (gab3 != "C") and (gab3 != "D") and (gab3 != "E"):
    print("Resposta Inválida!")
    gab3 = input("Gabarito 3: ").upper()

gab4 = input("Gabarito 4: ").upper()
while (gab4 != "A") and (gab4 != "B") and (gab4 != "C") and (gab4 != "D") and (gab4 != "E"):
    print("Resposta Inválida!")
    gab4 = input("Gabarito 4: ").upper()

gab5 = input("Gabarito 5: ").upper()
while (gab5 != "A") and (gab5 != "B") and (gab5 != "C") and (gab5 != "D") and (gab5 != "E"):
    print("Resposta Inválida!")
    gab5 = input("Gabarito 5: ").upper()

gab6 = input("Gabarito 6: ").upper()
while (gab6 != "A") and (gab6 != "B") and (gab6 != "C") and (gab6 != "D") and (gab6 != "E"):
    print("Resposta Inválida!")
    gab6 = input("Gabarito 6: ").upper()

gab7 = input("Gabarito 7: ").upper()
while (gab7 != "A") and (gab7 != "B") and (gab7 != "C") and (gab7 != "D") and (gab7 != "E"):
    print("Resposta Inválida!")
    gab7 = input("Gabarito 7: ").upper()

gab8 = input("Gabarito 8: ").upper()
while (gab8 != "A") and (gab8 != "B") and (gab8 != "C") and (gab8 != "D") and (gab8 != "E"):
    print("Resposta Inválida!")
    gab8 = input("Gabarito 8: ").upper()

gab9 = input("Gabarito 9: ").upper()
while (gab9 != "A") and (gab9 != "B") and (gab9 != "C") and (gab9 != "D") and (gab9 != "E"):
    print("Resposta Inválida!")
    gab9 = input("Gabarito 9: ").upper()

gab10 = input("Gabarito 10: ").upper()
while (gab10 != "A") and (gab10 != "B") and (gab10 != "C") and (gab10 != "D") and (gab10 != "E"):
    print("Resposta Inválida!")
    gab10 = input("Gabarito 10: ").upper()

print("\n--- INÍCIO DA PROVA PARA OS ALUNOS ---")

while continuar == "S":
    # Zerar a nota a cada novo aluno
    nota = 0 
    
    # Questão 1
    resp = input("Questão 1: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 1: ").upper()
    if resp == gab1:
        nota = nota + 1

    # Questão 2
    resp = input("Questão 2: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 2: ").upper()
    if resp == gab2:
        nota = nota + 1

    # Questão 3
    resp = input("Questão 3: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 3: ").upper()
    if resp == gab3:
        nota = nota + 1

    # Questão 4
    resp = input("Questão 4: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 4: ").upper()
    if resp == gab4:
        nota = nota + 1

    # Questão 5
    resp = input("Questão 5: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 5: ").upper()
    if resp == gab5:
        nota = nota + 1

    # Questão 6
    resp = input("Questão 6: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 6: ").upper()
    if resp == gab6:
        nota = nota + 1

    # Questão 7
    resp = input("Questão 7: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 7: ").upper()
    if resp == gab7:
        nota = nota + 1

    # Questão 8
    resp = input("Questão 8: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 8: ").upper()
    if resp == gab8:
        nota = nota + 1

    # Questão 9
    resp = input("Questão 9: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 9: ").upper()
    if resp == gab9:
        nota = nota + 1

    # Questão 10
    resp = input("Questão 10: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E"):
        print("Resposta Inválida!")
        resp = input("Questão 10: ").upper()
    if resp == gab10:
        nota = nota + 1

    # Verificação de maior e menor nota
    if nota > maiorNota:
        maiorNota = nota
    if nota < menorNota:
        menorNota = nota

    # Atualização dos totais e controle do loop
    somaNotas = somaNotas + nota
    totalAlunos = totalAlunos + 1
    
    # Imprimindo a nota usando a variável 'nota' corretamente
    print("Aluno %d tirou a nota %d" %(totalAlunos, nota))
    
    continuar = input("Deseja continuar (S/N)? ").upper()

# Resultados finais
if totalAlunos > 0:
    media = somaNotas / totalAlunos
    print("\nO total de alunos que utilizaram o sistema é: %d" %totalAlunos)
    print("A media dos alunos é de: %.1f" %media)
    print("A maior nota é de: %.1f" %maiorNota)
    print("A menor nota é de: %.1f" %menorNota)
else:
    print("Nenhum aluno registrado.")
    
print("Fim do programa")