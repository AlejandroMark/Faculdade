#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
#calcular a média alcançada por aluno e apresentar a mensagem:
#Aprovado", se a média alcançada for maior ou igual a sete;
#Reprovado", se a média for menor do que sete;
#Aprovado com Distinção", se a média for igual a dez.

n1 = int(input("Informe uma nota: "))
n2 = int(input("Informe outra nota: "))

media = (n1 + n2) /2 

if media == 10:
    print("Aprovado com Distinção %.2f" %(media))
else:
    if media >= 7:
        print("Aprovado %.2f" %(media))
    else:
        if media < 7:
            print("Reprovado %.2f" %(media))
