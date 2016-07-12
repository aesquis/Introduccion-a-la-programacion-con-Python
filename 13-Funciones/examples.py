##Defining a function, start with def then define a descriptive name 
#def holaAmics():
#    print('Hola Amics')
#    #return it means exit
#    return

#holaAmics()
#------------------------------------------------
##funcio main
##Definie this function
##When someone calls this function, execute this code
#def main():
#    holaAmics()
#    return

#def holaAmics():
#    print('Hola Amics')
#    return

##Execute the main function
##In order to do that the function must be executed
#main()
#------------------------------------------------
#def main():
#    mostraNoms()
#    return

#def mostraNoms():
#    names = ['Albert','Santi','Jordi']
#    for name in names:
#        print(name)
#    return

#main()
#------------------------------------------------
#Function with parameters
#def main():
#    names = ['Albert', 'Santi','Jordi']
#    newName = input('Enter last Guest: ')
#    names.append(newName)
    
#    printNames(names)
#    return

#def printNames(names):
#    for name in names:
#        print(name)
#    return
#------------------------------------------------
#def getMessage(name):
#    message = 'Hello, ' + name
#    return message

#def printMessage(message):
#    print(message)
#    return

#output = getMessage ('Christopher')
#printMessage(output)
#---------------------------------------------------
def main():
    names = getNames()
    printNames(names)
    return

def getNames():
    names = ['Albert', 'Santi','Jordi']
    newName = input('Enter last Guest: ')
    names.append(newName)
    return names


def printNames(names):
    for name in names:
        print(name)
    return
main()

