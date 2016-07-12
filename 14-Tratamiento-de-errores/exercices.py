import sys

fileName = input("Nom del fitxer que vols veure: ")
try :
    file = open (fileName, "r")
    allFileContent = file.read()
    print(allFileContent)
except FileNotFoundError:
    print("El fitxer que indiques no s'ha trobat")
    create = input('Vols crear el fitxer amb el nom indicat? Si/No: ').upper()
    if create == ('SI'):
        file = open(fileName, mode = "w")
        file.close()

except:
        error = sys.exc_info()[0]
        print(error)

finally:
    print('Operancio finalitzada amb exit')
