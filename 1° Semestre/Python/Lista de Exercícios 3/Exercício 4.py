'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; (maiúsculas e minúsculas)
'''

nome = input("Informe o nome: ")
while len(nome) <= 3:
    print("Nome inválido!")
    nome = input("Informe o nome: ")

idade = int(input("Informe a idade: "))
while idade < 0 or idade > 100:
    print("Idade inválida!")
    idade = int(input("Informe a idade: "))

salario = float(input("Informe o salário: "))
while salario <= 0:
    print("Salário inválido!")
    salario = float(input("Informe o salário: "))

sexo = input("Informe o sexo [f/m]: ")
while sexo != "f" and sexo != "m":
    print("Sexo inválido!")
    sexo = input("Informe o sexo [f/m]: ")

estadoC = input("Informe o estado civil [s/c/v/d]: ").lower()
while estadoC != "s" and estadoC != "c" and estadoC != "v" and estadoC != "d":
    print("Estado civil inválido!")
    estadoC = input("Informe o estado civil [s/c/v/d]: ").lower()

print("\nNome: %s" %nome)
print("Idade: %d" %idade)
print("Salário: %.2f" %salario)
print("Sexo: %s" %sexo)
print("Estado Civil: %s" %estadoC)