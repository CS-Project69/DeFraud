from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import phonenumbers
import string
import nltk

# Create your views here.
def index(request):
    return render(request,'index.html')
def call(request):
    return render(request,'main.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact us.html')
