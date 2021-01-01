from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import phonenumbers
import string
import nltk
nltk.download()

# Create your views here.
def index(request):
    return render(request,'index.html')
def call(request):
    return render(request,'main.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact us.html')

stopwords = nltk.corpus.stopwords.words('english')
punctuation = string.punctuation

def read():
    data = pd.read_csv('SPAM.txt', sep = '\t', header=None, names=["label", "sms"])
    '''nltk.download('stopwords')
    nltk.download('punkt')'''
    return data

def pre_process(sms):
    remove_punct = "".join([word.lower() for word in sms if word not in punctuation])
    tokenize = nltk.tokenize.word_tokenize(remove_punct)
    remove_stopwords = [word for word in tokenize if word not in stopwords]
    return remove_stopwords

def emailv(request):
    spam_counter = 0
    ham_counter = 0
    spam_words = []
    ham_words = []
    data=read()
    stopwords = nltk.corpus.stopwords.words('english')
    punctuation = string.punctuation
    if request.method=='GET':
        return render(request,'emailv.html')
    if request.method=='POST':
        emailbody=request.POST['emailbody']
        phoneno=request.POST['phoneno']
        if len(phoneno)==13:
            from phonenumbers import geocoder
            phone_number = phonenumbers.parse(phoneno) 
            country = geocoder.description_for_number(phone_number,'en')
            from phonenumbers import carrier
            service_provider = phonenumbers.parse(phoneno)
            carry=carrier.name_for_number(service_provider,'en')
        di={}
        di['some']=carry
        di['some1']=country
        remove_punct = "".join([word.lower() for word in emailbody if word not in punctuation])
        tokenize = nltk.tokenize.word_tokenize(remove_punct)
        remove_stopwords = [word for word in tokenize if word not in stopwords]
        data['processed'] = data['sms'].apply(lambda x: pre_process(x))
        #Handling messages associated with spam
        for emailbody in data['processed'][data['label'] == 'spam']:
            for word in emailbody:
                spam_words.append(word)
        #Handling messages associated with ham
        for emailbody in data['processed'][data['label'] == 'ham']:
            for word in emailbody:
                ham_words.append(word)
                
        for i in emailbody:
            spam_counter += spam_words.count(i)
            ham_counter += ham_words.count(i)
        blacklist = ["Nigeria","Armenia","Uganda","New Zealand"]
        if country in blacklist:
            spam_counter = spam_counter + 12
        if ham_counter > spam_counter:
            accuracy = round((ham_counter / (ham_counter + spam_counter) * 100))
            di['some2']=accuracy
            return render(request,'notspam.html',di)
        elif ham_counter == spam_counter:
            accuracy = round((ham_counter / (ham_counter + spam_counter) * 100))
            di['some2']=accuracy
            return render(request,'halfspam.html',di)
        else:
            accuracy = round((spam_counter / (ham_counter + spam_counter)* 100))
            di['some2']=accuracy
            return render(request,'fullspam.html',di)
            
            
    
    
        



