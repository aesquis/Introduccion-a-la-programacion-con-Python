def crearFitxer():
    nom = nomArxiu()
    data = dataArxiu()
    creaArxiu(nom, data)
    return

def nomArxiu():
    nom = input('Com vols que es digui el fitxer? ')
    return nom

def dataArxiu():
    data = input('Que vols escriure en el fitxer? ')
    return data


def creaArxiu(nom, data):
    fileName = nom
    WRITE = 'w'
    file = open(fileName, mode = WRITE)
    file.write(data)
    file.close()

crearFitxer()
print('Fitxer ceart correctament')

#Microsoft----------------------
def writeText(data, filename):
    file = open(filename, mode = 'w')
    file.write(data)
    return

writeText('Hello, world.', 'c:\\users\\chharri\\documents\\hello.txt')
