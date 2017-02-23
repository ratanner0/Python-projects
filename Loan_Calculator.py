# The following is being used for a loan calculator
# Monthly payment formula is:
# M = L[i(1+i)n]/[(1+i)n-1]
# M = monthly payment
# L = Loan Amount
# i = interest rate (for an interest rate of 5%, i = 0.05)
# n = number of payments
M = 1.00
L = input("Please enter the amount of your loan: \n")
# Converts user input in string format into a float
L = float(L)
i = input("Please enter the interest rate for the loan.\n" + 
          "Example: if 5.5%, please type 5.5 \n")
# Converts user input in string format into a float
i = float(i)/100/12
n = input("Please enter the number of payments. \n")
# Converts user input in string format into a float
n = float(n) 
M = L * ((i * ((1+i) ** n)) / ((1+i) ** n - 1))
''' Prints the string of monthly payment and converts the 
monthly payment to 2 decimal places'''
print ("Your monthly payment will be $%.2f" %(M))