#Importem la classe locale i l'idioma del sistema
import locale
locale.setlocale(locale.LC_ALL, '')

#Importem la classe de data i hora
import datetime

#Guardem la data local en una varialble
dataActual = datetime.date.today()

#Preguntem a l'usuari per la data límit del projecte.
userInput = input('Si us plau, indiqui la data limit del projecte (dd/mm/yyyy): ')

#Convertim la resposta de l'usuari en una data
fiProjecte = datetime.datetime.strptime(userInput, '%d/%m/%Y').date()

#Restem els dies que falten
dies = fiProjecte - dataActual

#Creem la cadena de resposta inserint només un resultat numèric amb els dies
print('Queden un total de %d dies fins a la fi del projecte' %dies.days)

#Iniciem càlcul de setmanes
#Dividim els dies restatns entre 7
setmanes = (dies.days) / 7
#Convertim el resultat a nombre integre
intSetmanes = int(setmanes)
#print (intSetmanes)

#calculem el dies restants a les setmanes
dies = (dies.days)%7
intDies = int(dies)
#print(intDies)

#Motrem resultats en dies i setmanes
print('Aixo suposen untotal de {0:d} setmanes i {1:d} dies'.format (intSetmanes,intDies))
#El mateix però amb un altre format
print('Aixo suposen untotal de 1%d setmanes i 2%d dies' %(intSetmanes,intDies))
