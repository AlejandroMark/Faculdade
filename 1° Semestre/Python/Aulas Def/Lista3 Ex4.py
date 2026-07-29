#LISTA 3 - ex. 4

def lerNome():
    print ("INFORME OS CAMPOS ABAIXO PARA SEREM VALIDADOS.")
    pare = False
    while not pare:
        nome = input("NOME (maior que 3 caracteres): ")
        if len(nome) > 3:
            pare = True
        else:
            print("Nome inválido!")        
    
    return nome  


def lerIdade():        
    pare = False        
    while not pare:
        idade = (int)(input("IDADE (entre 0 e 150 anos): "))
        if idade > 0 and idade <= 150:
            pare = True
        else:
            print("Idade inválida!")          

    return idade  

def lerSalario():        
    pare = False
    while not pare:
        salario = (float)(input("SALÁRIO (maior que 0): "))
        if salario > 0:
            pare = True
        else:
            print("Salário inválido!")   

    return salario


def lerSexo():       
    pare = False
    while not pare:
        sexo = (input("SEXO (F ou M): "))
        sexo = sexo.lower()  # converte para minúsculo
        if sexo == 'f' or sexo == 'm':
            pare = True
        else:
            print("Sexo inválido!")  
    
    return sexo


def lerEstCivil():        
    pare = False
    while not pare:
        estCivil = (input("ESTADO CIVIL (S, C, V, D): "))
        estCivil = estCivil.lower()
        if estCivil == 's' or estCivil == 'c' or estCivil == 'v' or estCivil == 'd':
            pare = True
        else:
            print("Estado Civil inválido!")     

    return estCivil       




def main():
    nome = lerNome()
    idade = lerIdade()
    salario = lerSalario()
    sexo = lerSexo()
    estCivil = lerEstCivil()
    
    print ("NOME: %s\nIDADE: %s\nSALÁRIO: R$ %4.2f\nSEXO: %c\nESTADO CIVIL: %c" %(nome,idade,salario,sexo,estCivil))

main()