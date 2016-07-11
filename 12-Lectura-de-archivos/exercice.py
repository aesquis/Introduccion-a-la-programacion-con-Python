#Llegir linia a linia tot el fitxer
import csv
filename = "llista.csv"
accessmode = "r"

#opening using with mantain the file closed, and help to prevent errors of opened files. you don't have to remember to close
with open(filename, accessmode) as mycsvfile:
    #read the file content
    datafromfile = csv.reader(mycsvfile,  delimiter=";")
    #creo un bucle per agafar linia a linia
    for llistat in datafromfile:
        print(' - '.join (llistat))
#-----------------------------------
