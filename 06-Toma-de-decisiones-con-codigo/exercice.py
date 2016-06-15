#coding:windows-1252
#Importem la classe locale i l'idioma del sistema
import locale
locale.setlocale(locale.LC_ALL, '')

# Declaració de variables
freeShipping = False

# Consulta de importa a l'usuri convertint la cadena en enter
compra = float(input("Quin és l'import total de la seva compra? "))
if compra > 50 :
    # Si la compra és superior a 50 la variable freeShipig es verdadera
    freeShipping = True

# Quan freeShipping és true, mostrem l'import sense afegir càrrec de transport
if freeShipping :
    print("Apreciat client, l'import total de la seva compra es de ${:,.2f} , moltes gràcies per la seva confiança".format(compra))

# En cas de que freeShipping no sigui True, sumem 10 $ a la comanda.
else :
    print("\nApreciat client,  l'import total de la seva compra es de ${:,.2f}" .format(compra))
    print("\nmés 10$ per el carrec de transport.2")
    print("\nAixo suma un total de ${:,.2f} ".format(compra + 10.00))
print("\nQue tingui un bon dia\n")
