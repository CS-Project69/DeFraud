#pan card verification
import random
import mysql.connector as sql
con=sql.connect(host="localhost",user="root",passwd="Samarth123",database="samarth")
mycursor=con.cursor

pan=str(input("enter pan card number: "))
fname=str(input("enter first name in capital: "))
lname=str(input("enter last name in capital: "))
n=len(pan)
l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

a=lname[0]
l2=["1","2","3","4","5","6","7","8","9","0"]
l3=["C","P","H","F","A","T","B","L","J","G"]
s=0
captcha=""
l4=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","0"]
for i in range(10):
    y=random.randint(0,61)
    captcha=captcha+l4[y]
print(captcha)
cap=str(input("enter the captcha: "))


    
if n==10 and cap==captcha:
    for i in range(0,5):
        if pan[i] in l:
            s=s+1
    for j in range(5,10):
        if pan[j] in l2:
            s=s+1

    if s==9 and pan[9] in l:
        if pan[4]==lname[0] and pan[9] in l:
            if pan[3] in l3:
                print("pan card is verified")
            else:
                print("enter again")
        else:
            print("enter again")
    else:
        print("not valid")
elif n==10 and cap!=captcha:
    print("captcha entered wrong")
else:
    print("not valid")
            
    
