Master_Card = ["51","52","53","54","55"]
American_Express = ["34","37"]
check1 = 0
check2 = 0

def luhn_algorithm(n):
     global check1
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
          check1 = 1
     else:
          check1 = 0
     return check1


def publisher(string):
     global check2

     if len(string) ==16:
          print("Alright! So far so good")
          p = str(input("Enter the mentioned publisher of your card (present in the bottom right corner) in full CAPITALS: "))
          if p == "VISA":
               if string[0] == 4:
                    check2 = 1
               else:
                    check2 = 0
          elif p == "MASTER CARD":
               if string[0:2] in Master_Card:
                    check2 = 1
               else:
                    check2 = 0
          elif p == "AMERICAN EXPRESS":
               if string[0:2] in American_Express:
                    check2 = 1
               else:
                    check2 = 0
     else:
          print("Please enter a valid Credit Card Number, it must be a 16 digit number for the tool to work!")
     return check2
