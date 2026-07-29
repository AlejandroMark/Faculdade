'''
Faça um programa com funções para ler o nome do aluno e suas três notas. Valide a
entrada das notas. Calcule a média final do aluno e imprima: “APROVADO” se a média for
maior ou igual a 7; “REPROVADO” se a média for menor que 6; e “PROVA FINAL” se a
média estiver entre 6 e 7. Imprima também as notas na ordem decrescente. Faça uma
função para cada operação: ler o nome; ler e validar as notas; calcular a média; imprimir a
mensagem e imprimir as notas na ordem decrescente. 
'''

def lerNome():
    nome = input("Informe o nome do aluno: ")
    return nome

def lerNota():
    nota = float(input("Informe a nota: "))
    
    while nota < 0 or nota > 10:
        print("Nota inválida!")
        nota = float(input("Informe a nota: "))
        
    return nota

def calcularMedia(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def imprimirMensagem(media):
    if media >= 7:
        print("APROVADO")
    elif media < 6:
        print("REPROVADO")
    else:
        print("PROVA FINAL")

def imprimirNotas(n1, n2, n3):
    notas = [n1, n2, n3]
    notas.sort(reverse=True)

    print("\nNotas em ordem decrescente:")
    print(notas[0])
    print(notas[1])
    print(notas[2])

nome = lerNome()

nota1 = lerNota()
nota2 = lerNota()
nota3 = lerNota()

media = calcularMedia(nota1, nota2, nota3)

print("\nNome:" %nome)
print("Média:" %media)

imprimirMensagem(media)
imprimirNotas(nota1, nota2, nota3)