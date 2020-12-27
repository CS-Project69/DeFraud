from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def call(request):
    return render(request,'main.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact us.html')
mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]
def Validate(aadharno):
    try:
        i = len(aadharno)
        j = 0
        x = 0

        while i > 0:
            i -= 1
            x = mult[x][perm[(j % 8)][int(aadharno[i])]]
            j += 1
        if x == 0:
            return True
        else:
            return False

    except ValueError:
        return 'Invalid Aadhar Number'
    except IndexError:
        return 'Invalid Aadhar Number'


def aadhar(request):
    if request.method=='GET':
        return render(request,'aadhar.html')
    if request.method=='POST':
        aadharno=request.POST['Aadhar']
        
        
        while True:
            if aadharno == 'exit':
                break
            elif (len(aadharno) == 12 and aadharno.isdigit()):
                x=Validate(aadharno)
                if x==True:
                    return render(request,'valid.html')
                elif x==False:
                    return render(request,'invalid.html')
            else:
                return render(request,'invalid.html')
        


