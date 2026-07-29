'''
Faça um programa que leia um nome de usuário e a sua senha. 
A senha não pode ser igual ao nome do usuário, nem menor que 6 caracteres. 
Caso ocorra o erro, mostre a mensagem de erro e volte a pedir as informações. 
No final imprima o nome e a senha.
'''

nome = input("Informe o nome: ")
senha = input("Informe a senha: ")

while senha == nome or len(senha) < 6:

    if senha == nome:
        print("Erro! A senha não pode ser igual ao nome.")

    if len(senha) < 6:
        print("Erro! A senha deve ter pelo menos 6 caracteres.")

    senha = input("Informe outra senha: ")

print("O Nome é: %s" %nome)
print("A Senha é: %s" %senha)