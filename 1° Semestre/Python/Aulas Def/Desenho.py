import turtle

##################
def desenharDegrau():
    turtle.color('#00FF00')
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)



##################
def desenharLado():
    cont = 1
    while cont <= 3:
        desenharDegrau()
        cont = cont + 1



### PROGRAMA PRINCIPAL #########
def main():
    cont = 1
    while cont <= 4:
        desenharLado()
        turtle.right(90)
        cont = cont + 1


main()
