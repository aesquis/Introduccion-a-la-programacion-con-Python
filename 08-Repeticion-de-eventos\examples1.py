#turtle commands
# right(x)      Rotate right x degrees
# left(x)       Rotate left x degrees
# color('x')    Change pen color to x
# forward(x)    Move forward x
# backward(x)   Move backward x

#import turtle
#turtle.color('green')
#turtle.forward(100)
#turtle.right(45)
#turtle.color('blue')
#turtle.forward(50)
#turtle.right(45)
#turtle.color('pink')
#turtle.forward(100)

#Draw a square
#import turtle
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)

#Draw a square with a loop
#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#turtle.color('red')
#turtle.forward(200)

#Loop in a loop
#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range (4):
#        turtle.forward(50)
#        turtle.right(90)
#        for moresteps2 in range (4):
#            turtle.forward(25)
#            turtle.right(90)

#import turtle
#for steps in range(5):
#    turtle.forward(100)
#    turtle.right(365/5)
#    for moresteps in range(5):
#        turtle.forward(50)
#        turtle.right(360/5)

#import turtle
#nbrSides = 5
#for steps in range(nbrSides):
#    turtle.forward(100)
#    turtle.right(360/nbrSides)
#    for moresteps in range(nbrSides):
#        turtle.forward(50)
#        turtle.right(360/nbrSides)

## Aixo retornara 1 2 3 
#for steps in range(1,4):
#    print (steps)

# Aixo retornara 1 3 5 7 9 
#for steps in range(1,10,2):
#    print (steps)

#Això retornara 1 2 3 4 5, notar que no hi ha range i tenim claus ator
#for steps in [1,2,3,4,5] :
#    print (steps)

#import turtle
#for steps in ['red','blue','green','black']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)

import turtle
for steps in ['red','blue','green','black',8]:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)
