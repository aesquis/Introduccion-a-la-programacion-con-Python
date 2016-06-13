#In this case if my answer is 500 and 75 the result is going to be 50075, because
#the nuambers are stored as a string
salary = input("please enter your salary ")
bonus = input("please enter your bonus ")
paycheckAmount = salary + bonus
print(paycheckAmount)

#There are functions to convert from one datatype to another
#int(Value)  converts to an integer
#long(Value) converts to a long integer
#float(value) converts to a floting number
    #(i.e. a niumber that can hold decimal places)
#str(value) converts to a string

salary = input("please enter your salary ")
bonus = input("please enter your bonus ")
paycheckAmount = float(salary) + float(bonus)
print(paycheckAmount)
