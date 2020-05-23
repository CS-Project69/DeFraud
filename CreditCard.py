#Credit Card Validation
print("---------------------------------------------------------\nWELCOME TO THE CREDIT CARD VALIDATION TOOL\n---------------------------------------------------------")

n = int(input("Please begin by entering the Credit Card Number:  "))
string = str(n)
a = str(n)
if len(a) ==16:
     
     print("Yoww")
     p = str(input("Enter the mentioned publisher of your card (present in the bottom right corner) in full CAPITALS: "))
     if p == "VISA":
          for i in string:
               if i[0] == 4:
                    check1 = 1
               else:
                    check1 = 0
                    
            
          
          
     
#Module calling
else:
     print("Please enter a valid Credit Card Number, it must be a 16 digit number")


