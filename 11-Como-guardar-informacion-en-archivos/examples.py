# access mode
# r         Read the file
# w         Write the file
# a         Append the file
# b         Open a binary file
# w+        Significa lectura/esccriptura
#fileName = 'demo.txt'
#WRITE = 'w'
#READ = 'r'
#APPEND = 'a'
#READWRITE = 'w+'

#file = open(fileName, mode = WRITE)
#file.write("Hi there!\n") 
#file.write("How are you?")
#file.close()

#print('File written successfully')
#-----------------------------------------------------
fileName = 'demo.csv'
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'w+'

data = input('Please enter file info: ')
file = open(fileName, mode = WRITE)
file.write(data)
file.close()

print('File written successfully')
