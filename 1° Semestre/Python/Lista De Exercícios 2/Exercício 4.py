'''
Faça um programa que peça a hora atual e mostre uma mensagem na tela de acordo com
os intervalos abaixo:
0 <= Hora < 5  “VAI DORMIR ...”
5 <= Hora < 12  “BOM DIA”
12 <= Hora < 18  “BOA TARDE”
18 <= Hora < 24  “BOA NOITE”
Outro valor  “HORA INVÁLIDA”
'''

hora = int(input("Informe a hora: "))

if hora >= 0 and 5 > hora:
    print("Vai dormir já é %.2f Horas!" %(hora))
elif hora >= 5 and 12 > hora:
    print("Bom dia já é %.2f" %(hora))
elif hora >= 12 and 18 > hora:
    print("Boa tarde já é %.2f" %(hora))
elif hora >=18 and 24 > hora:
    print("Boa noite já é %.2f" %hora)
else:
    print("Hora Inválida")