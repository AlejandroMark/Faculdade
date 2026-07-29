'''
Criar um programa que a partir da idade e peso do paciente calcule a dosagem de determinado medicamento e imprima a receita 
informando quantas gotas do medicamentoo paciente deve tomar por dose. Considere que o medicamento em questão possui 500mg por ml, e que cada ml corresponde a 20 gotas. 
Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ouacimade60 quilos devem tomar 1000 mg; com peso abaixo de 60 quilos, devemtomar 875mg.
Para crianças e adolescentes abaixo de 12 anos, a dosagem é calculada pelo peso corpóreo conforme a tabela a seguir:
'''

idade = int(input("Informe a idade: "))
peso = float(input("Informe o peso: "))

if idade >= 12:
    if peso >= 60:
        mg = 1000
        print("Dosagem: %d mg" %(mg))
    else:
        mg = 875
        print("Dosagem: %d mg" %(mg))
else:
    if peso >= 5 and peso <= 9:
        mg = 125
        print("Dosagem: %d mg" %(mg))
    elif peso >= 9.1 and peso <= 16:
        mg = 250
        print("Dosagem: %d mg" %(mg))
    elif peso >= 16.1 and peso <= 24:
        mg = 375
        print("Dosagem: %d mg" %(mg))
    elif peso >= 24.1 and peso <= 30:
        mg = 500
        print("Dosagem: %d mg" %(mg))
    else:
        mg = 750
        print("Dosagem: %d mg" %(mg))

ml = mg / 500
gotas = ml * 20
print("Quantidade de gotas: %.0f gotas" % gotas)