def lerNome():
    nome = input("Nome do cliente: ")
    while nome.replace(" ","").isalpha() != True:  
        print("NOme inválido!")
        nome = input("Nome do cliente: ")
    return nome


def lerNumeroInt():
    num = input("Número inteiro: ")
    while num.isdigit() == False :
        print ("Número inteiro inválido!")
        num = input("Número inteiro: ") 
    return int(num)


def lerNumeroReal():
    num = input("Número real: ")
    while num.replace(".","",1).isdigit() == False :
        print ("Número real inválido!")
        num = input("Número real: ")
    return float(num)



#### PRINCIPAL ####

print("Nome: %s" %lerNome() )
print("Número inteiro: %d " %lerNumeroInt() )
print("Número real: %f" %lerNumeroReal() )