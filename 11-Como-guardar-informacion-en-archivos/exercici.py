#------Exercici----------------------
# Definim el fitxer i l'obrim
fileName = 'llista.csv'
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'w+'

#Defineixo variables
nomConv = ('')
nombre = 1

file = open(fileName, mode = WRITE)
print('Entra el nom i edat de cada un dels convidats\n')
#Mentre la variable nomConv sigui diferent de FI s'executa el loop
#Un dels problemes principals era que al escriure FI, encar em demanava l'edat un cop i això ho escribia al fitxer
#ara primer inicio el loop i amb l'if posterior controlo que en cas de que el nom sigui FI, ho puc tallar al moment
#sense escriure res al fitxer ni demanar l'edat del FI
while nomConv != 'FI':
    nomConv = input('Nom %d: ' %nombre)
    if nomConv != 'FI':
        edat = input('Edat: ')
        strNombre = str(nombre)
        file.write(strNombre)
        file.write('; ' + nomConv +'; '+ edat + '\n')
        nombre = nombre ++ 1
print('Llista completada correctament')
file.close()
