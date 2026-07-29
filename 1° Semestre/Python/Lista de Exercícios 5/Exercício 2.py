'''
Altere o exercício 10 da Lista 4 para usar funções. Será necessário apenas uma função
para ler e validar a resposta (“A”, “B”, “C”, “D”, “E”). Essa função será chamada 10 vezes,
uma vez para cada questão, para preencher o gabarito e depois será chamada mais 10
vezes para ler as respostas dos alunos.
'''

def lerResposta():
    resposta = input("Resposta: ").upper()

    while resposta != "A" and resposta != "B" and resposta != "C" and resposta != "D" and resposta != "E":
        print("Resposta inválida!")
        resposta = input("Resposta: ").upper()

    return resposta


gabarito = []
cont = 1

print("GABARITO")

while cont <= 10:
    print("Questão", cont)
    gabarito.append(lerResposta())
    cont += 1

respostasAluno = []
cont = 1

print("\nRESPOSTAS DO ALUNO")

while cont <= 10:
    print("Questão", cont)
    respostasAluno.append(lerResposta())
    cont += 1

acertos = 0
cont = 0

while cont < 10:
    if gabarito[cont] == respostasAluno[cont]:
        acertos += 1
    cont += 1

print("Quantidade de acertos:", acertos)