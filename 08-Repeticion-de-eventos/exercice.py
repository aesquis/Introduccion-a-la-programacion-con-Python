#Consultem nombre de cares
cares = input('Cuantes cares vols que tingui la figura?')
#Convertim cadena en enter
caresRange = int(cares)
#Dibuixem
import turtle
for steps in range (caresRange):
    turtle.forward(100)
    turtle.right(360/caresRange)
    for steps in range (caresRange):
        turtle.forward(50)
        turtle.right(360/caresRange)
