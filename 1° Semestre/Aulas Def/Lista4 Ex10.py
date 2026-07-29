# LISTA 4 - ex. 10

# Informar as repostas de um prova e
# comparar com o gabarito

def lerResposta():
    resp = input("Questão: ").upper()
    while (resp != "A") and (resp != "B") and (resp != "C") and (resp != "D") and (resp != "E") :
        print("Resposta inválida!")
        resp = input("Questão: ").upper()
    
    return resp



##### PROGRAMA PRINCIPAL ##############
maiorNota = -1
menorNota = 9999
totalAlunos = 0
somaNotas = 0

print("PROFESSOR, informe o gabarito da prova:")

gab1 = lerResposta()
gab2 = lerResposta()
gab3 = lerResposta()
gab4 = lerResposta()
gab5 = lerResposta()
gab6 = lerResposta()
gab7 = lerResposta()
gab8 = lerResposta()
gab9 = lerResposta()
gab10 = lerResposta()


continuar = "S"
while continuar == "S" :
    # Leitura das RESPOSTAS das 10 questões de UM aluno

    nota = 0
    print("RESPOSTAS do aluno: ")

    #----------------
    # QUESTÃO 1
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab1:
        nota = nota + 1
    

    #----------------
    # QUESTÃO 2
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab2:
        nota = nota + 1

    #----------------
    # QUESTÃO 3
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab3:
        nota = nota + 1        

    #----------------
    # QUESTÃO 4
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab4:
        nota = nota + 1
  
  
    #----------------
    # QUESTÃO 5
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab5:
        nota = nota + 1

    #----------------
    # QUESTÃO 6
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab6:
        nota = nota + 1


    #----------------
    # QUESTÃO 7
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab7:
        nota = nota + 1

    #----------------
    # QUESTÃO 8
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab8:
        nota = nota + 1


    #----------------
    # QUESTÃO 9
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab9:
        nota = nota + 1

    #----------------
    # QUESTÃO 10
    #----------------
    resp = lerResposta()
    
    # Comparar com gabarito
    if resp == gab10:
        nota = nota + 1


    # Calculo MAIOR nota
    if nota > maiorNota:
        maiorNota = nota

    # Calculo MENOR nota
    if nota < menorNota:
        menorNota = nota

    somaNotas = somaNotas + nota
    totalAlunos = totalAlunos + 1

    print("Aluno %d tirou a nota %d" %(totalAlunos, nota) )

    # Deseja continuar
    continuar = input("Deseja continuar (S/N)? ").upper()


media = somaNotas / totalAlunos
print("Maior nota: %.1f" %maiorNota)
print("Menor nota: %.1f" %menorNota)
print("Total de alunos: %.1f" %totalAlunos)
print("Média : %.1f" %media)
print("FIM DO PROGRAMA")