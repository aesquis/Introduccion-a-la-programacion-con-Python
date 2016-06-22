# The "elif" alloes you to check fo different values

country = input("Where ara you from? ").upper()

if country == "CANADA" :
    print("Hello")
elif country == "GERMANY" : 
    print("Guten Tag")
elif country == "FRANCE" :
    print("Bonjour")
else :
    print("You are a " + country + " loser")
