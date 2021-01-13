from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.
def index(request):
    return render(request,'index.html')
def call(request):
    return render(request,'main.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='GET':
        return render(request,'contact us.html')
    if request.method=='POST':
        f=request.POST['firstname']
        s=request.POST['secondname']
        feed=request.POST['feedback']
        c=request.POST['country']
        with open('feedback.csv','a') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([f,s,c,feed])
        return render(request,'thankyou.html')    
            
