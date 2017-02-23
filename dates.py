'''Challenge
Ask a user to enter the deadline for their project
Tell them how many days they have to complet the project
For extra credit, give them the answer as a combination of weeks 
and days(Hint: you will need some of the math functions from the 
module on 
numeric values)'''
#Imports the datetime function
import datetime
#saves the current date 
todaysDate = datetime.datetime.now().date()
userDateInput=input("Please enter the date in which your project is due. Format mm/dd/yyyy\n")
#converts the string entered by the user into a date format
dueDate=datetime.datetime.strptime(userDateInput,"%m/%d/%Y").date()
deadline=dueDate-todaysDate
#converts the deadline into days
daysUntil=deadline.days
#print(daysUntil)
#converts the deadline into weeks
weeksUntil=deadline.days/7
#print("%.2f"%(weeksUntil))
#converts the deadline into years
yearsUntil=deadline.days/365
#Prints the number of days, weeks, and years until a project is due
print("Your project will be due in " + "%d "%(daysUntil) + "days")
print()
print("You have " + "%.2f "%(weeksUntil) + "weeks until the project is due.")
print()
print("You have " + "%.2f "%(yearsUntil) +"years left until the project due date.")

