#coding:windows-1252

#primer declara les variables, ja que en cas de no fer-ho, 
#si deposit és < 100 la variable freeToaster no existiria i  el codi donaria erroro
freeToaster = False

#Booleanas
deposit = int(input("How much do you want to deposit? "))
if deposit > 100 :
    #Set the boolean variables freeToaster to True  
    freeToaster=True

#if the variable freeToaster is True
#the print statement will execute
if freeToaster :
    print("Enjoy your toaster!")
print("Have a nice day")
