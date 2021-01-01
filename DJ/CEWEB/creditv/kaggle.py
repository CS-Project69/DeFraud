import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def kaggle1():
     file = input("Enter name of the file with transactional entries: ")
     data = pd.read_csv(file)


     #Analysis
     fraud = data[data['Class'] == 1]
     valid = data[data['Class'] == 0]

     Fraction = len(fraud)/float(len(valid))
     print("Fraction of fraudulent entries: ",Fraction) 
     print("Fraud Cases: {}".format(len(fraud)))
     print("Valid Transactions: {}".format(len(valid)))

     #Checking
     list1 = []
     for i in list1:
          list1.append(fraud["Time"])
     print (list1)

     inp = int(input("Enter the time code of the transaction you want to check: "))
     if inp in list1:
          print("Fraud")
          
     else:
          print("Not Fraud")

     #Graphical Plot
     count_classes = pd.value_counts(data['Class'], sort=True)
     count_classes.plot(kind='bar', rot=0)
     plt.title("Distributed Transactions")
     plt.xticks(range(2), ['Normal', 'Fraud'])
     plt.xlabel("Class")
     plt.ylabel("Frequency")
     plt.show()

     #Details 
     print("Details of the fraudulent transactions")
     print("----------------------")
     print(fraud.Amount.describe())

     print("Details of valid transactions")
     print("----------------------")
     print(valid.Amount.describe())
