def lerNota(ind):
    num = input("Nota %d: " % ind)
    while (num.replace(".", "", 1).isdigit() == False) or (float(num) < 0) or (float(num) > 10):
        print("Nota inválida!")
        num = input("Nota %d: " % ind)
    return float(num)

def cadastrarNotas(vetNotas):
    pos = 0
    while pos < 5:
        nota = lerNota(pos + 1)
        vetNotas.append(nota)
        pos = pos + 1

def mostrarNotas(vetNotas):
    pos = 0
    while pos < len(vetNotas):
        print("Nota %d: %.1f" % (pos + 1, vetNotas[pos]))
        pos = pos + 1

def calcularMedia(vetNotas):
    soma = 0
    pos = 0
    while pos < len(vetNotas):
        soma = soma + vetNotas[pos]
        pos = pos + 1
    return soma / len(vetNotas)

def maiorNota(vetNotas):
    maior = vetNotas[0]
    pos = 1
    while pos < len(vetNotas):
        if vetNotas[pos] > maior:
            maior = vetNotas[pos]
        pos = pos + 1
    return maior

def menorNota(vetNotas):
    menor = vetNotas[0]
    pos = 1
    while pos < len(vetNotas):
        if vetNotas[pos] < menor:
            menor = vetNotas[pos]
        pos = pos + 1
    return menor

def mostrarAcimaMedia(vetNotas, media):
    pos = 0
    print("Notas acima da média:")
    while pos < len(vetNotas):
        if vetNotas[pos] > media:
            print("%.1f" % vetNotas[pos])
        pos = pos + 1

def main():
    vetNotas = []
    cadastrarNotas(vetNotas)
    mostrarNotas(vetNotas)

    media = calcularMedia(vetNotas)
    maior = maiorNota(vetNotas)
    menor = menorNota(vetNotas)
    print("MÉDIA: %.2f" % media)
    mostrarAcimaMedia(vetNotas, media)
    print("MAIOR: %.2f" % maior)
    print("MENOR: %.2f" % menor)
main()