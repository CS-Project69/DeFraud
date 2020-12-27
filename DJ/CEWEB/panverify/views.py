from django.shortcuts import render
from django.http import HttpResponse
import random
import string
'''from streamlit import caching
caching.clear_cache()'''
# Create your views here.
def index(request):
    return render(request,'index.html')
def call(request):
    return render(request,'main.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact us.html')
captcha=''
def captcha1():
    global captcha
    l4=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","0"]
    for i in range(10):
        y=random.randint(0,61)
        captcha=captcha+l4[y]
    return captcha   
    


def panv(request):
    global captcha
    if request.method=='GET':
        captcha=captcha1()
        return render(request, 'pan.html', {'captcha': captcha})    
    if request.method=='POST':
        panno=request.POST['Panno']
        fname=request.POST['first']
        lname=request.POST['second']
        cap=request.POST['captchas']
        x=fname.upper()
        y=lname.upper()
        n=len(panno)
        l2=["1","2","3","4","5","6","7","8","9","0"]
        l3=["C","P","H","F","A","T","B","L","J","G"]
        s=0
        l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        if n==10 and cap==captcha:
            for i in range(0,5):
                if panno[i] in l:
                    s=s+1
            for j in range(5,10):
                if panno[j] in l2:
                    s=s+1
            if s==9 and panno[9] in l:
                if panno[4]==y[0] and panno[9] in l:
                    if panno[3] in l3:
                        captcha=''
                        return render(request,'verified.html')
                    else:
                        captcha=''
                        return render(request,'pan.html')
                else:
                    captcha=''
                    return render(request,'pan.html')
            else:
                captcha=''
                return render(request,'notverified.html')
            
        else:
            captcha=''
            return render(request,'notverified.html')
            
    elif n==10 and cap!=captcha:
        captcha=''
        return render(request,'notverified.html')
        
    else:
        captcha=''
        return render(request,'notverified.html')
    

