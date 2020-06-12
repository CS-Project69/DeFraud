#luhn's algorithm

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
    
    
