import datetime    
#Get time and print time


currentTime = datetime.datetime.now()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)


print (datetime.datetime.strftime(currentTime, '%H:%M'))
# %H Hours (24 hr clock)
# %l Hours (12 hr clock)
# %p AM or PM
# %m Minutes
# %S Seconds
