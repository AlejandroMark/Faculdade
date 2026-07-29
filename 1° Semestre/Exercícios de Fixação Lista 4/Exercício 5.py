'''
Altere os exercícios 1, 2, 3, 4, 6, 7 e 8 da Lista 4 para usar funções. 
Coloque apenas as funções para ler as informações. 
Será necessário uma função para cada informação a ser lida.
'''

#### EXERCíCIOS 6 ####

def lerProduto(n):
    # Recebe o contador para mostrar o número do produto
    valor = float(input("Produto %d: R$ " % n))
    return valor

def lerDinheiro():
    dinheiro = float(input("Dinheiro: R$ "))
    return dinheiro

# Loop principal para repetir o processo de novas compras
while True:
    print("Lojas Tabajara")
    total = 0
    contador = 1
    
    # Loop de cada compra
    while True:
        produto = lerProduto(contador)
        if produto == 0:
            break
        total += produto
        contador += 1
        
    print("Total: R$ %.2f" % total)
    
    # Leitura do valor pago
    dinheiro = lerDinheiro()
    troco = dinheiro - total
    print("Troco: R$ %.2f" % troco)
    print("--- Nova compra ---")