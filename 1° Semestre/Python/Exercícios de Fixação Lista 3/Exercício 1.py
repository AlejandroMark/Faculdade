'''
Altere os exercícios 3, 4, 5, 6 e 8 da Lista 3 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 3 ####
def lernome():
    nome = input("Informe o nome: ")
    return nome

def lersenha():
    senha = input("Informe a senha: ")
    return senha

def main():
    while senha == nome or len(senha) < 6:
        if senha == nome:
            print("Erro! A senha não pode ser igual ao nome.")
        if len(senha) < 6:
            print("Erro! A senha deve ter pelo menos 6 caracteres.")
        senha = input("Informe outra senha: ")

nome = lernome()
senha = lersenha()

print("Nome: %s" %nome)
print("Senha: %s" %senha)