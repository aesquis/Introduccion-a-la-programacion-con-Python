name = input("What is your name ? ")
print('Hello ' + name)
name = input('And now ? ')
print('Hello ' + name)
#Variables no poden conteir espais, són case sensitive i no poden começar amb un número

firstName = input('What is your first Name ? ')
lastName = input ('what is your last Name ? ' )
print("Hello" + " " +firstName + " " + lastName)

animal = input("What is your favourite animal? ")
building = input ("Name a famous buildint: ")
color = input("What is your favourite color? ")
print("Hickory Dickory Dock!")
print("The "+color+" "+animal+" ran up the "+building)

message = 'Hello world'
#Tot en minúscules
print(message.lower())
#Tot en Majúscules
print(message.upper())
#Invertir entre majúscules i minúscules
print(message.swapcase())

name = input("What is your name? ")
country = input("What is your country? ")
country = country.upper()
print('Hello,\n '+ name +' Form '+ country)

message = 'hello world'
print(message.find('world'))
print(message.count('o'))
print(message.capitalize())
print(message.replace('hello','Hi'))

message = 'hello world'
print(message.find('world'))
print(message.count('o'))
print(message.capitalize())
print(message.replace('hello','Hi'))

postalCode = " "
postalCode = input("Please enter your postal code: ")
print(postalCode.upper())

