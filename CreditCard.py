#Credit Card Validation
print("---------------------------------------------------------\nWELCOME TO THE CREDIT CARD VALIDATION TOOL\n---------------------------------------------------------")

n = int(input("Please begin by entering the Credit Card Number:  "))
string = str(n)
Master_Card = ["51","52","53","54","55"]
American_Express = ["34","37"]

#Publisher Check
if len(a) ==16:
     print("Yoww")
     p = str(input("Enter the mentioned publisher of your card (present in the bottom right corner) in full CAPITALS: "))
     if p == "VISA":
          if string[0] == 4:
               check1 = 1
          else:
               check1 = 0
     elif p == "MASTER CARD":
          if string[0:2] in Master_Card:
               check1 = 1
          else:
               check1 = 0
     elif p == "AMERICAN EXPRESS":
          if string[0:2] in American_Express:
               check1 = 1
          else:
               check1 = 0
if check1 == 0:
     print("Your card number does not belong to the specified publisher, it possibly a fraudulent card")
continue          
     
#Module calling
else:
     print("Please enter a valid Credit Card Number, it must be a 16 digit number for the tool to work!")


