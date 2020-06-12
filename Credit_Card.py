#Credit Card Validation
print("---------------------------------------------------------\nWELCOME TO THE CREDIT CARD VALIDATION TOOL\n---------------------------------------------------------")

n = int(input("Please begin by entering the Credit Card Number:  "))
string = str(n)
Master_Card = ["51","52","53","54","55"]
American_Express = ["34","37"]

#Publisher Check
if len(a) ==16:
     print("Done")
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
     
 def luhn_algorithm():
    n=str(input("enter credit card number: "))
    l=[]
    l2=[]
    l3=[]
    c1=0
    c2=0

    m=n[::-1]
    for i in range(len(m)):
        a=int(m[i])
        l.append(a)
    
    for i in range(1,len(l),2):
        b=l[i]*2
        l2.append(b)
    
    
    for i in l2:
        sod = sum(int(digit) for digit in str(i))
        l3.append(sod)
    

    for i in l3:
        c1=c1+i
    for i in range(2,len(l),2):
        c2=c2+l[i]
    c=c1+c2
    

    x=(c*9)%10
    if x==l[0]:
        print("valid")
    else:
        print("not valid")

luhn_algorithm()


