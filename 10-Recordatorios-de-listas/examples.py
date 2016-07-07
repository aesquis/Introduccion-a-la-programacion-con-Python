#Llistes

#-----------------------------------------------------------------

#guests = ['Christopher','Susan','Bill','Satya']
#print(guests[0])

#-----------------------------------------------------------------

#score = [23,45,67,23,54,14,98]
#print(score[3])

#-----------------------------------------------------------------

#Podem contar en sentit invers amb negatius. Aixo retornara 98
#score = [23,45,67,23,54,14,98]
#print(score[-1])

#-----------------------------------------------------------------

#guests = ['Christopher','Susan','Bill','Satya']
#print(guests[0])
#print(guests[1])

#-----------------------------------------------------------------
##Substituir un valor
#guests = ['Christopher','Susan','Bill','Satya']
#print ("First values is " + guests[0])

##Change the first value in the list to Steve
#guests[0] = 'Steve'
#print ("First values is now " + guests[0])

#-----------------------------------------------------------------
##Afegir un valor al final de la llista
#guests = ['Christopher','Susan','Bill','Satya']

##Add a new value to the end of a list
#guests.append('Steve')
#print(guests[-1])

##-----------------------------------------------------------------
##Eliminar un valor
#guests = ['Christopher','Susan','Bill','Satya']
##Remove a new value to the end of a list
#guests.remove('Christopher')
#print(guests[0])

##-----------------------------------------------------------------
##Eliminar un valor per posicio
#guests = ['Christopher','Susan','Bill','Satya']
##Remove a new value to the end of a list
#del guests [0]
#print(guests[0])

#--------------------------------------------------------------------
#guests = ['Christopher','Susan','Bill','Satya']

#guests.remove('Satya')
#del guests[0]
#print (guests[0])
#print (guests[-1])


##Add a value
#guests.append('Colin')
#guests.append('Sonia')

##Update a value
#guests[3] = 'Sonal'

#print (guests[3])
#print (guests[-1])
#
#-------------------------------------------------------------------
#Cercar en la llista
#Si crequem un valor que no existeix el programa peta
guests = ['Christopher','Susan','Bill','Satya']
print(guests.index('Bill'))
