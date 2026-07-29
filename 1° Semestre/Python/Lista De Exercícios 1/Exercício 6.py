#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dis = int(input("Distância percorrida (km): "))
vel = int(input("Velocidade média (km/h): "))

tempo = dis / vel

print("O tempo estimado de viagem é de %.2f horas" %(tempo))