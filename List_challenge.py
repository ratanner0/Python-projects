'''
Ask the user to enter the names of everyone attending a party

Then return a list of the party guests in alphabetical order'''

#Creates the guests variable
guests=[]
#Asks user to enter the name of the first guest
guests.append(input("Please enter the name of the first guest. "))
#Asks user if they want to add additional guests
moreGuests=input("Would you like to add more guests?  Y or N ")
#Checks the entry from the user to continue  if not Y or y it leaves the loop
while moreGuests == "Y" or moreGuests=="y":
    guests.append(input("Please enter the name of your next guest. "))
    moreGuests=input("Would you like to add more guests?  Y or N ")
#Sorts the list into alphabetical order
guests.sort()
#Prints the sorted guest list
for guest in guests:
    print(guest)