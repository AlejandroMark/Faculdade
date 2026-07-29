'''
Altere os exercícios 1, 2, 3, 4, 6, 7 e 8 da Lista 4 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 7 ####

# Variáveis para acumular dados e controlar a contagem
contador = 0
somaAltura = 0
somaPeso = 0

def lerCodigo():
    codigo = int(input("Informe o código do cliente: "))
    return codigo

def lerAltura():
    altura = float(input("Informe a altura: "))
    return altura

def lerPeso():
    peso = float(input("Informe o peso: "))
    return peso

while True:
    codigo = lerCodigo()
    # Encerra o programa se o código for 0
    if codigo == 0:
        break
    
    altura = lerAltura()
    peso = lerPeso()
    contador += 1
    
    somaAltura += altura
    somaPeso += peso

    # Define os valores iniciais na primeira entrada
    if contador == 1:
        maiorAltura = menorAltura = altura
        maiorPeso = menorPeso = peso
        codigoMaiorAltura = codigoMenorAltura = codigo
        codigoMaiorPeso = codigoMenorPeso = codigo

    # Compara e atualiza os extremos (maior/menor)
    if altura > maiorAltura:
        maiorAltura = altura
        codigoMaiorAltura = codigo

    if altura < menorAltura:
        menorAltura = altura
        codigoMenorAltura = codigo

    if peso > maiorPeso:
        maiorPeso = peso
        codigoMaiorPeso = codigo

    if peso < menorPeso:
        menorPeso = peso
        codigoMenorPeso = codigo

# Calcula as médias finais
mediaAltura = somaAltura / contador 
mediaPeso = somaPeso / contador

# Exibe os resultados formatados
print("\nCLIENTE MAIS ALTO")
print("Código: %d" % codigoMaiorAltura)
print("Altura: %.2f" % maiorAltura)

print("\nCLIENTE MAIS BAIXO")
print("Código: %d" % codigoMenorAltura)
print("Altura: %.2f" % menorAltura)

print("\nCLIENTE MAIS GORDO")
print("Código: %d" % codigoMaiorPeso)
print("Peso: %.2f" % maiorPeso)

print("\nCLIENTE MAIS MAGRO")
print("Código: %d" % codigoMenorPeso)
print("Peso: %.2f" % menorPeso)

print("\nMédia das alturas: %.2f" % mediaAltura)
print("Média dos pesos: %.2f" % mediaPeso)