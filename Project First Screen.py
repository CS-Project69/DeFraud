def emailvalidation():
    print("You have chosen the email validation option.")

def creditcardverification():
    print("You have chosen the credit card verification option.")

def menu():
    ch=int(input("enter 1 for email validation or enter 2 for credit card verification:"))
    if ch==1:
        E=emailvalidation()
        

    elif ch==2:
        C=creditcardverification()
        

    else:
        print('enter a valid choice')
        menu()

menu()        
        
    
    

     
