#open my file
#animalFile = open("tazmania.txt", "r")
##read all file contents
#allFileContents = animalFile.read()
#print(allFileContents)
#-----------------------------------
#animalFile = open("tazmania.txt", "r")
##Show first line
#firstAnimal = animalFile.readline()
#print(firstAnimal)
##Show first line
#secondAnimal = animalFile.readline()
#print(secondAnimal)
#-----------------------------------
#import csv
#dataFromFile = csv.reader(myCSVFile, delimiter=";")
#-----------------------------------
#Llegir linia a linia tot el fitxer
#import csv
#fileName = "llista.csv"
#accessMode = "r"

##opening using with mantain the file closed, and help to prevent errors of opened files. You don't have to remember to close
#with open(fileName, accessMode) as myCSVFile:
#    #Read the file content
#    dataFromFile = csv.reader(myCSVFile,  delimiter=";")
#    #Creo un bucle per agafar linia a linia
#    for llistat in dataFromFile:
#        print(llistat)
#-----------------------------------
#import csv
#with open("tazmania.txt","r") as animalFile :
#    allRowsList = csv.reader(animalFile)

#    for currentRow in allRowsList :
#        print(currentRow)
#-----------------------------------
#import csv
#with open("tazmania.txt","r") as animalFile :
#    allRowsList = csv.reader(animalFile)

#    for currentRow in allRowsList :
#        print(currentRow)
#        for currentWord in currentRow:
#            print(currentWord)
#-----------------------------------
import csv
with open("tazmania.txt","r") as animalFile :
    allRowsList = csv.reader(animalFile)

    for currentRow in allRowsList :
        print(' -'.join (currentRow))
