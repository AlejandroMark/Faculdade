def menu():
    op = ""
    # Valida se a opção é um número e está entre 0 e 6
    while op.isdigit() == False or int(op) < 0 or int(op) > 6:
        print("\n" * 50) # Limpa a tela
        print("SISTEMA DE INVESTIMENTO")
        print("1 - Inserir investimento")
        print("2 - Pesquisar por código")
        print("3 - Rendimento")
        print("4 - Maior investimento")
        print("5 - Excluir")
        print("6 - Listar")
        print("0 - Sair")
        op = input("Escolha sua opção: ")
    return int(op)

#Função para pesquisar retornando o índice
def pesquisar(vetor_codigos, cod_pesq):
    i = 0
    while i < len(vetor_codigos):
        if vetor_codigos[i] == cod_pesq:
            return i
        i = i + 1
    return -1

def inserir(vetor_codigos, vetor_valores):
    cod = int(input("Digite o código do investimento: "))
    
    # Verifica se o código já existe reaproveitando a função pesquisar
    pos = pesquisar(vetor_codigos, cod)
    if pos != -1:
        print("Erro: Já existe um investimento com este código.")
        return

    valor = float(input("Digite o valor investido: R$ "))
    while valor <= 0:
        print("Erro: O valor investido deve ser maior que zero.")
        valor = float(input("Digite o valor investido: R$ "))

    #Adiciona os novos elementos ao final do vetor
    vetor_codigos.append(cod)
    vetor_valores.append(valor)
    print("Investimento cadastrado com sucesso!")

def rendimento(vetor_codigos, vetor_valores):
    cod = int(input("Digite o código do investimento para atualizar: "))
    pos = pesquisar(vetor_codigos, cod)
    
    if pos == -1:
        print("Investimento não encontrado.")
    else:
        porcentagem = float(input("Digite a porcentagem de aumento (%): "))
        aumento = vetor_valores[pos] * (porcentagem / 100)
        vetor_valores[pos] = vetor_valores[pos] + aumento
        print("Rendimento aplicado! Novo valor: R$ %.2f" % vetor_valores[pos])

def maior_investimento(vetor_codigos, vetor_valores):
    if len(vetor_valores) == 0:
        print("Não há investimentos cadastrados.")
        return

    indice_maior = 0
    i = 1
    while i < len(vetor_valores):
        if vetor_valores[i] > vetor_valores[indice_maior]:
            indice_maior = i
        i = i + 1
        
    print("Maior Investimento -> Código: %d | Valor: R$ %.2f" % (vetor_codigos[indice_maior], vetor_valores[indice_maior]))

def excluir(vetor_codigos, vetor_valores):
    cod = int(input("Digite o código do investimento que deseja excluir: "))
    pos = pesquisar(vetor_codigos, cod)
    
    if pos == -1:
        print("Investimento não encontrado.")
    else:
        #Remove o elemento passando a posição (índice) do vetor
        del(vetor_codigos[pos])
        del(vetor_valores[pos])
        print("Investimento excluído com sucesso!")

def listar(vetor_codigos, vetor_valores):
    if len(vetor_codigos) == 0:
        print("Não há investimentos cadastrados.")
        return
        
    print("--- LISTA DE INVESTIMENTOS ---")
    i = 0
    while i < len(vetor_codigos):
        print("Código: %d - Valor: R$ %.2f" % (vetor_codigos[i], vetor_valores[i]))
        i = i + 1

###### PRINCIPAL ##########
def main():
    codigos = []
    valores = []
    op = 1
    while op != 0:
        op = menu()
        if op == 0:
            print("\n\nFim do programa!!!\n\n")

        elif op == 1:
            print("\n\nINSERIR\n\n")
            # Chamar a função para Inserir os dados nos vetores
            inserir(codigos, valores)

        elif op == 2:
            print("\n\nPESQUISAR\n\n")
            # Ler a informação para pesquisar
            cod = int(input("Digite o código para pesquisar: "))
            # Chamar a função para pesquisar no vetor
            pos = pesquisar(codigos, cod)
            # Imprimir os dados se encontrar
            if pos != -1:
                print("Investimento Encontrado -> Código: %d | Valor: R$ %.2f" % (codigos[pos], valores[pos]))
            else:
                print("Investimento não encontrado.")

        elif op == 3:
            print("\n\nRENDIMENTO\n\n")
            # Chamar a função para aplicar o rendimento na posição pesquisada
            rendimento(codigos, valores)

        elif op == 4:
            print("\n\nMAIOR\n\n")
            # Chamar a função para pesquisar no vetor o maior elemento
            maior_investimento(codigos, valores)

        elif op == 5:
            print("\n\nEXCLUIR\n\n")
            # Chamar a função para pesquisar e excluir se encontrar
            excluir(codigos, valores)

        elif op == 6:
            print("\n\nLISTAR\n\n")
            # Listar todos os dados dos vetores
            listar(codigos, valores)

        else:
            print("Opção inválida!")

        input("Pressione <enter> para continuar ...")
        
main()