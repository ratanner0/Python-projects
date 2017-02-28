'''Calculate the total to charge for an order from an online store in Canada
Ask the user what country they are from and their order total
If the user is from Canada, ask which province
If the order is from outside Canada do not charge any taxes
If the order was placed in Canada calculate tax based on province
    Alberta charge 5% General sales Tax (GST)
    Ontario, New Brunswick, Nova Scotia charge 13% Harmonized sales tax
    All other provinces charge 6% provincial sales tax + 5%GST tax'''
#General Sales Tax of 5% for Alberta
GST=5/100
#Harmonized sales tax of 13% for Ontario, New Brunswick, Nova Scotia
HST=6/100
#Provincial sales tax of 6% plus General Sales tax of 5% for all others in Canada
PSTandGST=(6/100)+(5/100)
subtotalAmount=float(input("Please enter the total dollar amount of your purchase. \n"))
Country=input("Please enter the the country you are from. \n").upper()

if Country=="CANADA" :
    province=input("Which province in Canada? \n").upper()
    if province=="ALBERTA" :
        taxamount=(subtotalAmount*GST)
        total=(subtotalAmount*(GST+1))
        print("The tax amount is "+"$"+"%.2f"%(taxamount))
        print("Your total amount due is "+"$"+"%.2f"%(total))
    elif province=="ONTARIO" or province=="NEW BRUNSWICK" or province=="NOVA SCOTIA" :
        taxamount=(subtotalAmount*HST)
        total=(subtotalAmount*(HST+1)) 
        print("The tax amount is "+"$"+"%.2f"%(taxamount))
        print("Your total amount due is "+"$"+"%.2f"%(total))
    else :
        total=(subtotalAmount*(PSTandGST+1))
        taxamount=(subtotalAmount*PSTandGST) 
        print("The tax amount is "+"$"+"%.2f"%(taxamount))
        print("Your total amount due is "+"$"+"%.2f"%(total))
else :
    print("There are no additional taxes to your order")
    print("Your total amount due is "+"$"+"%.2f"%(subtotalAmount))