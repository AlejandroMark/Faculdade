# Ler e validar uma nota de ZERO a DEZ

nota = float ( input ("Informe sua nota: ") )
while nota < 0 or nota > 10 :
    print ("Nota inválida!") 
    nota = float ( input ("Informe sua nota: ") )

print ("Sua nota é: %.2f" %nota)