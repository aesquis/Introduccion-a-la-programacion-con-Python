# + Addition            5+2 = 7
# - Subtractin          5-2 = 3
# * Multiplication      5*2 = 10
# / Division            5/2 = 2.5
# ** Exponent           5**2 = 25
# % Modulo              5%2 = 1
#
# Order of operations
# () perentheses
# ** Exponent (e.g. **2 squared **3 cubed)
# */ multiplication and division
# + - addition and subtraction


#Basic functions
age = 42
print(age)
width = 20
height = 5
area = width * height
print(area)
perimeter = 2*width + 2*height
print(perimeter)
modulo = 45%5
print(modulo)

area = 0
height = 10
width = 20 
#Calculate the aread of a triangle
area = width * height /2

#print the area as a decimal
print("The area of the tiengle would be %d " % area)

#Syntax and Output
print('I have %d cats' % 6)        # I have 6 cats          - Convert to a decimal number
print('I have %3d cats' % 6)       # I have      6 cats     - Convert to a decimal with 6 digits long
print('I have %03d cats' % 6)      # I have 006 cats
print('I have %f cats' % 6)        # I have 6.000000 cats   - Convert to a Float
print('I have %.2f cats' % 6)      # I have 6.00 cats       - Convert to a float with 2 decimals

#print the are formated float avalue with 2  decimal places
print("The area of the tiengle would be %.2f " % area)

#print the area as a decimal
print("My favourite number is %d !" %13)

#print the area as a decimal with 6 digits long
print("My favourite number is %6d !" %13)

#print the area as a decimal with 6 digits long with leading zeros
print("My favourite number is %06d !" %13)

#You can also use a format method to format numeric values
print("I have {0:d} cats".format(6))    #I have 6 cats
print("I have {0:3d} cats".format(6))   #I have   6 cats
print("I have {0:03d} cats".format(6))  #I have 006 cats
print("I have {0:f} cats".format(6))    #I have 6.000000 cats
print("I have {0:.2f} cats".format(6))  #I have 6.00 cats

print("the area of the triangle would be {0:f} ".format(area))
print("My favourite number is {0:d} ".format(13))
# This is an example with multiple numbers
print("Here are three numbers! The firs is {0:d} The second is {1:4d} ans the last {2:d}".format(7,8,9))

#Slash \ in python means that the operation continues in the next line
total = 5 + 6 + 7 + 12 + 13 \
    +6 + 2
print("Total is %d" % total)

print("Here are three numbers! " + \
    "The first is {0:d} The second is {1:4d} ans the last {2:d}".format(7,8,9))
