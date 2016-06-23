#wonLottery = True
#bigWin = True

#if wonLottery and bigWin :
#    print("you can retire! ")

#team = input("enter your favourite hockey team; ").upper()
#sport = input("enter your favourite sport: ").upper()

#if sport == "football" and team == "barcelona":
#    print("putu amo")
#elif team == "madrid" or team =="atletico":
#    print("fck")

#else:
#    print("putu looser")

#if month == "Sep" or month =="Apr" \
#    or month == "Jun" or month == "Nov":
#    print("There are 30 days in this month")

#if favMovies == "Star Wars" \
#    and favBook == "Lord of the Rings" \
#    and favEvent == "ComicCon":
#    print("You and I should hang out")

#country = input("Where are you from ?").upper()
#pet = input("Which is your fabourite animal? ").upper()

#if country == "CATALONIA" and pet == "CAT" \
#    or pet == "DOG":
#    print("Is Barcelona your fabourite team?")


#if country == "CANADA" and \
#    pet == "MOOSE" or pet == "BEAVER" :
#    print("Do you play hockey too?")

team = input("Enter your favourite hockey team: ").upper()
sport = input("Enter your favourite sport: ").upper()

#If the sport is hockey and the team is senators or leafs, display the cup message
if sport == "HOCKEY" and (team == "SENATORS" or team == "LEAFS"):
    print ("Good luck getting the cup this year")


#Exemple simplificació

sportIsHockey = False
if sport == 'HOCKEY':
    sportIsHockey = True

teamIsCorrect = False
if team == 'SENATORS' or team == 'LEAFS':
    teamIsCorrect = True

if sportIsHockey and teamIsCorrect:
    print ("Good luck getting the cup this year")
