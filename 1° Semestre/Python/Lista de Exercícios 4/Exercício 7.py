'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
o mais gordo e o mais magro. Para isto você deve fazer um programa que pergunte a cada um dos clientes 
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dado quando o usuário 
digitar 0 (zero) no campo código. Ao encerrar o programa devem ser informados os códigos e valores do cliente mais alto, 
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
'''

contador = 0
somaAltura = 0
somaPeso = 0

while True:

    codigo = int(input("Informe o código do cliente: "))
    if codigo == 0:
        break
    altura = float(input("Informe a altura: "))
    peso = float(input("Informe o peso: "))
    contador += 1
     
    somaAltura += altura
    somaPeso += peso

    if contador == 1:
        maiorAltura = altura
        menorAltura = altura

        maiorPeso = peso
        menorPeso = peso

        codigoMaiorAltura = codigo
        codigoMenorAltura = codigo

        codigoMaiorPeso = codigo
        codigoMenorPeso = codigo

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

mediaAltura = somaAltura / contador 
mediaPeso = somaPeso / contador

print("\nCLIENTE MAIS ALTO")
print("Código:" %codigoMaiorAltura)
print("Altura:" %maiorAltura)

print("\nCLIENTE MAIS BAIXO")
print("Código:" %codigoMenorAltura)
print("Altura:" %menorAltura)

print("\nCLIENTE MAIS GORDO")
print("Código:" %codigoMaiorPeso)
print("Peso:" %maiorPeso)

print("\nCLIENTE MAIS MAGRO")
print("Código:" %codigoMenorPeso)
print("Peso:" %menorPeso)

print("\nMédia das alturas: %.2f" %mediaAltura)
print("Média dos pesos: %.2f" %mediaPeso)