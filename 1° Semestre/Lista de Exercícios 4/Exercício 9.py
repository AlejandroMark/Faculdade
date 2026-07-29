'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões de múltipla escolha. 
O programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e 
assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o 
sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
a. A maior e a menor nota;
b. O total de alunos que utilizaram o sistema;
c. A média das notas da turma.
Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
'''
maiorNota = -1
menorNota = 9999
totalAlunos = 0
somaNotas = 0
continuar = "S"
gab1 = "A"
gab2 = "B"
gab3 = "C"
gab4 = "D"
gab5 = "E"
gab6 = "E"
gab7 = "D"
gab8 = "C"
gab9 = "B"
gab10 = "A"

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