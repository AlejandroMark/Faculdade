'''
DESAFIO: Cassino. Altere o Jogo de Craps da questão anterior para que o jogador possa
apostar. Ele começa com R$ 100,00. No início de cada rodada ele informa quanto quer
apostar. Se perder, perde esse valor. Se ganhar, ganha o dobro do que apostou. No final
de cada rodada informe o total que ele tem em dinheiro e pergunte se quer continuar
jogando ou se quer parar
'''

import random

def lancarDado():
    return random.randint(1,6)

def jogarDados():
    input("Pressione ENTER para lançar os dados.")
    d1 = lancarDado()
    d2 = lancarDado()
    soma = d1 + d2
    print("Dado 1: %d" %d1)
    print("Dado 2: %d" %d2)
    print("SOMA: %d" %soma)
    print("---------------------")
    return soma

def proximaRodada(ponto):
    print("O seu PONTO é %d. Tente tirá-lo novamente para ganhar ou você perde se tirar 7." %ponto)

    while True:
        soma = jogarDados()

        if soma == ponto:
            print("Você tirou seu PONTO! Você GANHOU!")
            return True

        elif soma == 7:
            print("Você tirou 7! Você PERDEU!")
            return False

def primeiraRodada():
    dados = jogarDados()

    if dados == 7 or dados == 11:
        print("Você Ganhou!")
        return True

    elif dados == 2 or dados == 3 or dados == 12:
        print("Você Perdeu! Craps!")
        return False

    else:
        return proximaRodada(dados)

def main():
    dinheiro = 100.0
    continuar = "S"

    while continuar == "S" and dinheiro > 0:

        print("Você possui R$" %dinheiro)

        aposta = float(input("Informe o valor da aposta: "))

        while aposta > dinheiro or aposta <= 0:
            print("Aposta inválida!")
            aposta = float(input("Informe o valor da aposta: "))

        ganhou = primeiraRodada()

        if ganhou:
            dinheiro = dinheiro + aposta * 2
        else:
            dinheiro = dinheiro - aposta

        print("Total de dinheiro: R$", dinheiro)

        if dinheiro > 0:
            continuar = input("Deseja continuar jogando? (S/N): ").upper()

    print("Fim de jogo!")
    print("Você terminou com R$" %dinheiro)

main()