'''
Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança
um par de dados, obtendo a soma entre 2 e 12. Se na primeira jogada você tirar 7 ou 11,
você ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e
você perdeu. Se na primeira jogada você somou 4, 5, 6, 8, 9 ou 10, este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você
perde, no entanto, se tirar um 7 antes de tirar este “Ponto” novamente.
A função lancarDado() abaixo retorna um número aleatório entre 1 e 6 e
simula o lançamento de um dado.
A função jogarDados() simula uma jogada com os dois dados e retorna a
soma.
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
            break
        elif soma == 7:
            print("Você tirou 7! Você PERDEU!")
            break

def primeiraRodada():
    dados = jogarDados()
    
    if dados == 7 or dados == 11:
        print("Você Ganhou!")
    elif dados == 2 or dados == 3 or dados == 12:
        print("Você Perdeu! Craps!")
    else:
        proximaRodada(dados)

def main():
    primeiraRodada()

main()