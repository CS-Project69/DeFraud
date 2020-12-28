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

def read():
    data = pd.read_csv('SMSSpamCollection.txt', sep = '\t', header=None, names=["label", "sms"])
    nltk.download('stopwords')
    nltk.download('punkt')
    stopwords = nltk.corpus.stopwords.words('english')
    punctuation = string.punctuation

read()    
