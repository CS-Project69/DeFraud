from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import csv
import string
import matplotlib.pyplot as plt

def creditv(request):
    if request.method=='GET':
        return render(request,'creditcard.html')
    if request.method=='POST':
        credit=request.POST['Creditno']
        pubname=request.POST['Pubname']
        b = luhn_algorithm(credit)
        a = publisher(credit,pubname)
        if (a and b) == 1:
            return render(request,'valid1.html')
            

        if (a == 1) and (b == 0):
            return render(request,'wrongcredit1.html')
            print("The publisher and your card number match, but the card number is not verified. Please try to re-enter the number")

        if (a == 0) and (b == 1):
            return render(request,'wrongcredit2.html')
            print("The publisher and your card number do not match, it might possibly be a fraudulent card")

        if (a and b) == 0:
            return render(request,'wrongcredit3.html')
            print("Your credit card is possibly fraudulent")
            
    
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


def publisher(string,pubname):
     global check2

     if len(string) ==16:
          print("Alright! So far so good")
          p=pubname.upper()
          if p == "VISA":
               if string[0] == '4':
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

def valid(request):
    if request.method=='GET':
        return render(request,'valid1.html')
    if request.method=='POST':
        file=request.POST['filename']
        time=request.POST['timestamp']
        data = pd.read_csv(file)
        #Analysis
        fraud = data[data['Class'] == 1]
        valid = data[data['Class'] == 0]
        Fraction = len(fraud)/float(len(valid))
        st1=str(len(fraud))
        st2=str(len(valid))
        st3=str(Fraction)
        o=[st1,st2,st3]
        dictionary={}
        dictionary['some_string']=o[0]
        dictionary['some_other']=o[1]
        dictionary['other_other']=o[2]
        list1 = []
        with open(file,"r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[30] == "1":
                    list1.append(row[0])
        '''count_classes = pd.value_counts(data['Class'], sort=True)
        count_classes.plot(kind='bar', rot=0)
        plt.title("Distributed Transactions")
        plt.xticks(range(2), ['Normal', 'Fraud'])
        plt.xlabel("Class")
        plt.ylabel("Frequency")
        plt.show()'''

        labels = 'Not Fraud', 'Fraud'
        sizes = [99.8,0.2]
        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()
        if time in list1:
            return render(request,'fraud.html',dictionary)
        else:
            return render(request,'notfraud.html',dictionary)
        
    
   
    
    
