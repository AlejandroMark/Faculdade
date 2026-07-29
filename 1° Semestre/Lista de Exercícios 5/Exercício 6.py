'''
Faça um programa com uma função chamada somaImposto. A função possui dois
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem; e valorCusto, que é o custo de um item antes do imposto. A função retorna
o valor de custo acrescentado com o imposto sobre vendas. 
'''

def somaImposto(taxaImposto, valorCusto):
    return valorCusto + valorCusto * (taxaImposto / 100)

def lerValor():
    valor = float(input("Informe o valor do produto: "))
    while valor <= 0:
        print("Valor inválido!")
        valor = float(input("Informe o valor do produto: "))
    return valor

def lerTaxa():
    taxa = float(input("Informe a taxa de imposto (%): "))
    while taxa < 0:
        print("Taxa inválida!")
        taxa = float(input("Informe a taxa de imposto (%): "))
    return taxa

def main():
    valor = lerValor()
    taxa = lerTaxa()

    resultado = somaImposto(taxa, valor)

    print("Valor original: R$ %.2f" % valor)
    print("Taxa de imposto: %.2f%%" % taxa)
    print("Valor com imposto: R$ %.2f" % resultado)

main()