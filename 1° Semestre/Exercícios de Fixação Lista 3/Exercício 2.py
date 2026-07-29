'''
Altere os exercícios 3, 4, 5, 6 e 8 da Lista 3 para usar funções.
Coloque apenas as funções para ler as informações.
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 4 ####

def lerNome():
    nome = input("Informe o nome: ")
    while len(nome) <= 3:
        print("Nome inválido!")
        nome = input("Informe o nome: ")
    return nome

def lerIdade():
    idade = int(input("Informe a idade: "))
    while idade < 0 or idade > 150:
        print("Idade inválida!")
        idade = int(input("Informe a idade: "))
    return idade

def lerSalario():
    salario = float(input("Informe o salário: "))
    while salario <= 0:
        print("Salário inválido!")
        salario = float(input("Informe o salário: "))
    return salario

def lerSexo():
    sexo = input("Informe o sexo [f/m]: ").lower()
    while sexo != "f" and sexo != "m":
        print("Sexo inválido!")
        sexo = input("Informe o sexo [f/m]: ").lower()
    return sexo

def lerEstadoCivil():
    estadoC = input("Informe o estado civil [s/c/v/d]: ").lower()
    while estadoC != "s" and estadoC != "c" and estadoC != "v" and estadoC != "d":
        print("Estado civil inválido!")
        estadoC = input("Informe o estado civil [s/c/v/d]: ").lower()
    return estadoC

nome = lerNome()
idade = lerIdade()
salario = lerSalario()
sexo = lerSexo()
estadoC = lerEstadoCivil()

print("\nNome: %s" % nome)
print("Idade: %d" % idade)
print("Salário: %.2f" % salario)
print("Sexo: %s" % sexo)
print("Estado Civil: %s" % estadoC)