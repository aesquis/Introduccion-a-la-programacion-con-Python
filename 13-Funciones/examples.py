##First functions
#def main():
#    printMessage()
#    fck()
#    return

#def fck():
#    help = input("What the fuck ?") #This peace of shit works.
#    print(help)
#    return

#def printMessage():
#    print("Hello World")
#    return
##Funtion has to be defined before exection
#main() #Execute the main function
#---------------------------------------------------------------------#
#def main():
#    printNames()
#    return

#def printNames():
#    names = ['Albert','Jordi','Santi']
#    for name in names:
#        print (name)
#    return

#main()
#---------------------------------------------------------------------#
#def printMessage(message):  #This define de function whit a possible parameter
#    print(message)
#    return

#printMessage('Hello World') #This call de funcition with a paremeter
#---------------------------------------------------------------------#
#Multiple parametres funcio
#def displayMessage(felicitats, nom):
#    message = felicitats + ', ' + nom
#    print(message)
#    return
#displayMessage('Per molts anys', 'Albert')
#---------------------------------------------------------------------#
#def main():
#    names = ['Albert','Jordi', 'Santi'] #Definim la llista
#    newName = input('Insert a new name :') #preguntem per un nou nom i el posem en la variable newname
#    names.append(newName) #Afegim a la llista el nou nom guardat en la variable newName

#    printNames(names) #Cridem la funció printNames i li passaem el parametre (names) que es una variable
#    return

#def printNames(list): # definim la funcio printNames amb un parametre
#    for name in list: # fem un loop amb el parametre per a mostrar un llistat de noms
#        print(name)
#    return

#main() #cridem la funcio main
#----------------------------------------------------------------------#
##Es igual que l'anterior però en la funcio printNames posem el nom de parametre names per a demostrar que
##tot i tenir la varianble names definida en la funcio anterior, aquesta no surt de la funcio
#def main():
#    names = ['Albert','Jordi', 'Santi'] #Definim la llista
#    newName = input('Insert a new name :') #preguntem per un nou nom i el posem en la variable newname
#    names.append(newName) #Afegim a la llista el nou nom guardat en la variable newName

#    printNames(names) #Cridem la funció printNames i li passaem el parametre (names) que es una variable
#    return

#def printNames(names): # definim la funcio printNames amb un parametre
#    for name in names: # fem un loop amb el parametre per a mostrar un llistat de noms
#        print(name)
#    return

#main() #cridem la funcio main
#----------------------------------------------------------------------#
#Exit with a avalue
#def getMessage(name):
#    message = 'Hello, ' + name
#    return message

#def printMessage(message):
#    print(message)

#output = getMessage('Christopher')
#printMessage(output)
#----------------------------------------------------------------------#
def main():  # 1 - Definim funcio main
    
    names = getNames() #2 - definim la variable names que ontindra el resultat de la funcio getNames
    printNames(names) #4 - Cridem la funció printNames i li passaem el parametre (names) 
                      #que es una variable amb dades retornades per la funcio getNames
                      #Aquesta axecutarà la funcio printnames i els retornara a mode de llista
    return

def getNames(): #3 - Definim la funcio getNames
    names = ['Albert','Jordi', 'Santi'] #Definim la llista
    newName = input('Insert a new name :') #preguntem per un nou nom i el posem en la variable newname
    names.append(newName) #Afegim a la llista el nou nom guardat en la variable newName
    return names #Retornem a la consulta la variable names amb els resultats obtinguts a la funcio

def printNames(names2): # definim la funcio printNames amb un parametre que ens ve donat per la variable names obtinguda de la funcio getNames
    for name in names2: # fem un loop amb el parametre per a mostrar un llistat de noms
        print(name)
    return

main()
