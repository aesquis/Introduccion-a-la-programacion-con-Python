import datetime
currentDate = datetime.date.today()
#birthday = input ("What is your birthday? ")
#birthdate = datetime.strptime(birthday, "%m/%d/%Y").date()
##why did we list datetime twice?
##because we are calling the strptime function
##which is part of the datetime module
##which is in the datetime module
#print ("Your birthday is " + birthday.strftime('%B'))
userInput = input('Please enter your birthday (mm/dd/yyyy)')
birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
print(birthday)

days = birthday - currentDate
print(days.days)


