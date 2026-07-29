somaPeso = 0.0
somaAltura = 0.0
cont = 0
continuar = "S"
#menorAltura = 9999
#maiorAltura = -1

while continuar == "S" :

   	# Ler e validar peso
    peso = float ( input("Peso: ") )
    while peso <= 0 or peso >= 500 :
        print("Peso inválido!")
        peso = float ( input("Peso: ") )
    # Ler e validar altura
    while True :
        altura = float ( input("Altura: ")) 
        if altura > 0 and altura < 2.5 :
            break;
        else:
            print("Altura inválida!")
    if cont == 0:
        menorAltura = altura
        maiorAltura = altura
    if altura < menorAltura :   
        menorAltura = altura
    if altura > maiorAltura:
        maiorAltura = altura
    somaPeso = somaPeso + peso
    somaAltura = somaAltura + altura
    cont = cont + 1
    # Deseja continuar
    continuar = input("Deseja continuar (S/N)? ").upper()
mediaPeso = somaPeso / cont
mediaAltura = somaAltura / cont
print("Média dos pesos: %.2f"  %mediaPeso)
print("Média das alturas: %.2f"  %mediaAltura)
