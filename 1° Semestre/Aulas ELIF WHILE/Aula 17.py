# Ler a matrícula e o coeficiente de rendimento
# de um grupo de alunos e calcular a porcentagem
# dos que têm o coeficiente maior que 8.


continuar = "S"
cont = 0 	# Contador total
contMaior = 0 	# Contador maior que 8

while continuar == "S" :
    # Ler e validar a matricula
    mat = input ("Matricula:  ")

    # Ler e validar o coeficiente
    coeficiente = float (input ("Coeficiente: ") )
    while coeficiente < 0.0 or coeficiente > 10.0 :
        print ("Coeficiente inválido!")
        coeficiente = float (input ("Coeficiente: ") )

    if coeficiente > 8.0 :
        contMaior = contMaior + 1
    cont = cont + 1
		
    continuar = input ("Deseja continuar? (S/N) ")
    continuar = continuar.upper() 

print ("Estão acima de 8 %.2f %%."  %(contMaior*100/cont) )