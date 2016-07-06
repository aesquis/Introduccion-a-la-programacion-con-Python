#answer = "0"
#while answer != "4":
#    answer = input("What is 2+2? ")
#print ("Yes! 2+2 =$" )

#import turtle
#counter = 0
#while counter <4:
#    turtle.forward(100)
#    turtle.right(90)
#    counter = counter+1 
#    # counter += 1   (També funcionaria)

#Loops

#Import turtle
import turtle

#definim variables
midaLine = "null"
colorLine = "black"
angleLine = 0

#Consultem
midaLine = int(input("Allagada de la linia ? "))
colorLine = (input("Color de la linia ? ")).lower()
angleLine = int(input("Angle de la linia ? "))

#Fem el loop   

while midaLine != 0:
    #Consultem valors al usuari     
    turtle.color(colorLine)
    turtle.right(angleLine)
    turtle.forward(midaLine)
    #Tornem a preguntar perque no s'executi infinitament
    midaLine = int(input("Allagada de la linia ? "))
    #Fem un condicional
    if midaLine != 0 :
        colorLine = (input("Color de la linia ? ")).lower()
        angleLine = int(input("Angle de la linia ? "))
#Missatge final si posem un 0
print("Genial nano, ho has muntat molt be")
