"""Create a function to simplify writing to files
Set the function to accept parameters
-one for text
-one for the name of a file
Add the code that will write the text out to the file"""

import csv
WRITE="w"

def getNames ():
    name=[]
    next="Y"
    while next == "Y" or next == "y":
        name.append(input("Please enter the name of the person you would like to add. "))
        next = input("Would you like to enter another name? Y or N ")
    names=str(name)
    print(name)
    return names

def filePrint ():
    name = getNames()
    printName=open("functionChallenge.txt",WRITE)
    printName.write(name)
    printName.close()
    return 

filePrint()

print ("Your list have names have been printed successfully. ")
print ("The file is located in the directory ")

