import numpy as np
import pandas as pd 
import csv

def kaggle1():
     file = input("Enter name of the file with transactional entries: ")
     data = pd.read_csv(file)

     list1 = []
     
     with open(file,"r") as f:

          reader = csv.reader(f)
          for row in reader:
               if row[30] == "1":
                    list1.append(row[0])
                         
     #Analysis
     fraud = data[data['Class'] == 1]
     valid = data[data['Class'] == 0]

     Fraction = len(fraud)/float(len(valid))
     print("Fraction of fraudulent entries: ",Fraction) 
     print("Fraud Cases: {}".format(len(fraud)))
     print("Valid Transactions: {}".format(len(valid)))

     #Checking
     inp = input("Enter the time code of the transaction you want to check: ")
     if inp in list1:
            print("Fraud")
          
     else:
          print("Not Fraud")
kaggle1()
