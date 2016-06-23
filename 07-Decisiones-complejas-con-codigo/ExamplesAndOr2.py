#monday = True
#freshCoffe = False
#if monday :
#    #You could have a code here to check for fresh coffe

#    #the if statement is nested, so this if coffe
#    #is only executed if the other if statement is true
#    if not freshCoffe :
#        print("go buy a coffe!")
#    print ("I hate Mondays")
#print("now you can start work")

team = input("Enter your favourite hockey team: ").upper()
sport = input("Enter your favourite sport: ").upper()

if sport == "HOCKEY":
    print("Go hockey")
    if team == "SENATORS":
        print("Good luck getting to the cup!")
    print("We do love hoackey!")
