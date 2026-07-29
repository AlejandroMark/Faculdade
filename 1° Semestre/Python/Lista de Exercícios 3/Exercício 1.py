'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
No final imprima a nota.
'''

nota = float ( input ("Informe sua nota: ") )
while nota < 0 or nota > 10 :
    print ("Nota inválida!") 
    nota = float ( input ("Informe sua nota: ") )

print ("Sua nota é: %.2f" %nota)