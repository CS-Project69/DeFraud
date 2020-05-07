#Credit Card Validation
print("---------------------------------------------------------\nWELCOME TO THE CREDIT CARD VALIDATION TOOL\n---------------------------------------------------------")

n = int(input("Please begin by entering the Credit Card Number:  "))
a = str(n)
if len(a) ==16:
     
     print("Yoww")
     p = str(input("Enter the mentioned publisher of your card (present in the bottom right corner) : "))
     
#Module calling
else:
     print("Please enter a valid Credit Card Number, it must be a 16 digit number")


