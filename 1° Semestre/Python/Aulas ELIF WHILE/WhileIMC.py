# INICIALIZAR AS VARIÁVEIS
continuar = "S"
cont = 1

while continuar == "S":

    # LER a ALTURA e o PESO

    # VALIDAR A ALTURA
    altura = float(input("Altura: "))   
    while altura <= 0.1 or altura > 2.6 :
        print("Altura inválida!")
        altura = float(input("Altura: "))


    # VALIDAR O PESO
    peso = float(input("Peso: "))
    while peso < 10 or peso > 500:
        print("Peso inválido!")
        peso = float(input("Peso: "))

    imc = peso / pow(altura,2)

    print("Seu IMC é: %.2f"  %imc)

    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc < 25:
        print("Peso normal.")        
    elif imc < 30:
        print("Sobrepeso.")
    elif imc < 35:
        print("Obeso leve.")
    elif imc < 40:
        print("Obeso moderado.")
    else:
        print("Obeso mórbido.")
    
    cont = cont + 1

    continuar = input("Deseja continuar? (S/N)" ).upper()
    

print("FIM DO PROGRAMA")
