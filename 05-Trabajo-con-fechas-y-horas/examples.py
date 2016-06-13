#Import system language
import locale
locale.setlocale(locale.LC_ALL, '')

#The import statement gives us access to
#the functionality of the datetime class
import datetime

#today is a function tha returns today's date using datetime class proviously imported
print (datetime.date.today())
#Other example
currentDate = datetime.date.today()
print(currentDate)          #Returns 2016-06-13
print(currentDate.year)     #Returns 2016
print(currentDate.month)    #Returns 6
print(currentDate.day)      #returns 13
#strftime allows you to specify the date format
print (currentDate.strftime('%d %b,%Y')) #this is going to response 14 Jun, 2016

# %b is the month abbreviation
# %B is the full month name
# %y is two digit year
# %a is the day of the week abbreviated
# %A is the day of the week
print(currentDate.strftime('%b %B %y %a %A'))   # Jun June 16 Mon Monday
print(currentDate.strftime('%d, %b, %Y'))       # 13, Jun, 2016
print(currentDate.strftime ('Please attend our event %A, %B %d in the Year %Y')) #Please attend our event Monday, June 13 in the Year 2016
# Full list in strftime.org
