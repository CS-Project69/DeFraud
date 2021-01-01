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

'''def read():
    data = pd.read_csv('SMSSpamCollection.txt', sep = '\t', header=None, names=["label", "sms"])
    nltk.download('stopwords')
    nltk.download('punkt')
    stopwords = nltk.corpus.stopwords.words('english')
    punctuation = string.punctuation
read()    

def pre_process(sms):
    remove_punct = "".join([word.lower() for word in sms if word not in punctuation])
    tokenize = nltk.tokenize.word_tokenize(remove_punct)
    remove_stopwords = [word for word in tokenize if word not in stopwords]
    return remove_stopwords
data['processed'] = data['sms'].apply(lambda x: pre_process(x))

def categorize_words():
    spam_words = []
    ham_words = []
    #Handling messages associated with spam
    for sms in data['processed'][data['label'] == 'spam']:
        for word in sms:
            spam_words.append(word)
    #Handling messages associated with ham
    for sms in data['processed'][data['label'] == 'ham']:
        for word in sms:
            ham_words.append(word)
    return spam_words, ham_words

spam_words, ham_words = categorize_words()

spam_counter = 0
def predict(sms):
    ham_counter = 0
    #Count the occurances of each word in the sms string
    for word in sms:
        spam_counter += spam_words.count(word)
        ham_counter += ham_words.count(word)
    #If the message is ham
    if ham_counter > spam_counter:
        accuracy = round((ham_counter / (ham_counter + spam_counter) * 100))
        print('The entered input is not spam, with {}% certainty'.format(accuracy))
    #If the message could be equally spam and ham
    elif ham_counter == spam_counter:
        print('Message could be spam. There is a 50% chance!')
    #If the message is spam
    else:
        accuracy = round((spam_counter / (ham_counter + spam_counter)* 100))
        print('The entered input is spam, with {}% certainty'.format(accuracy))'''
