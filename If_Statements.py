'''Calculate shipping charges for a shopper
Ask the user to enter the amount for their total purchase
If their total is under $50 add $10, otherwise shipping if free
Tell the user their final total including shipping costs and format the number so it looks 
like a monetary value'''
#sets the subtotal to the float value the user inputs
subTotal = float(input("Please enter the total dollar amount for your purchase \n"))
#sets shipping to $10
shipping = 10
#if the amount entered by the user is greater than or equal to 50, run the code
if subTotal >=50:
    print ("You purchased " + "$"+"%.2f"%(subTotal) + " worth of product.")
    print ("Since you spent over $50.00 dollars, shipping is free.")
    print ("Your total comes to $"+"%.2f"%(subTotal))
#if the amount entered by the user is less than 50, run this code.
else:
    print ("You purchased " + "$"+"%.2f"%(subTotal) + " worth of product.")
    print ("Since your total amount came to less than $50.00,\nthere will be an additional shipping charge of $10.00")
    print ("Your total comes to " + "$"+"%.2f"%(subTotal + shipping))
print ("Thank you for shopping with us.  Have a wonderful day")

