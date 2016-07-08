#------Exercici----------------------
# Definim el fitxer i l'obrim
fileName = 'llista.csv'
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'w+'

nomConv = ('')
nombre = 1

file = open(fileName, mode = WRITE)
print('Entra el nom i edat de cada un dels convidats\n')
#Mentre la variable nomConv sigui diferent de FI s'executa el loop
while nomConv != 'FI':
    nomConv = input('Nom %d: ' %nombre)
    edat = input('Edat: ')
    strNombre = str(nombre)
    file.write(strNombre)
    file.write('; ' + nomConv +'; '+ edat + '\n')
    nombre = nombre ++ 1
print('Llista completada correctament')
file.close()
