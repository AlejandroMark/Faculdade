# Calcular a média de 5 notas de um aluno

soma = 0
cont = 1
while cont <= 5 :
    nota = float (input ("Digite uma nota: ") )
    soma = soma + nota
    cont = cont + 1

media = soma / 5
print ("A média é: %.2f"  %media)