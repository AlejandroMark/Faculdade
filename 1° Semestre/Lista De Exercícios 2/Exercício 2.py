#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra, escrever: F ­ Feminino, M ­ Masculino ou Sexo Inválido.

letra = input("Informe F ou M: ").upper()

if letra == "F":
    print("O sexo é Feminino: %s" %(letra))
elif letra == "M":
    print("O sexo é Masculino: %s" %(letra))
else:
    print("Sexo Inválido: %s" %(letra))