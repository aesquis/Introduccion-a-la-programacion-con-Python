#Llista de convidats a la festa

#definim llista convidats
convidats = ['']
print ('Entra el nom dels convidats, quan tinguis la llista complerta escui FI')
#definim variable intpConv per que no dongi error
intpConv = ('')
print('\n')
#Fem loop per a recollir dades

#Mentre la variable intpConv sigui diferent de Fi s'executa el loop
while intpConv != 'FI':
    intpConv = input('Convidat: ')
    #afegim el valor de la variable intpConv a la llista convidats
    convidats.append(intpConv)
#Eliminar registre FI de la llista FI
convidats.remove('FI')
#Ordenem la llista
convidats.sort()
print('\n')
print('Doncs aquests son tots els convidats de la teva llista')
#Fem un loop per a mostrar la llista
for llista in convidats:
    print(llista)
print('\n')
