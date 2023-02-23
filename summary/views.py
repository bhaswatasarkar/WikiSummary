from django.shortcuts import render
from django.http import HttpResponse
from .algorihms.bart import *
from .algorihms.sumy import *
from .algorihms.gensim import *
from .algorihms.gpt2 import *
from .algorihms.transformer import *
from .supportmodule.queryvalidator import *
from .supportmodule.text_extractor import *
from .supportmodule.extract_images import *
def homePage(request):
    return render(request,'home.html')

def outputPage(request):
    # base_url = "https://en.wikipedia.org/wiki/History_of_India"
    base_url = request.POST.get('url')
    if(base_url==""):
        return render(request,'home.html')
    
    option = int(request.POST.get('radio'))
    wordCount = request.POST.get('wordCount')
    ratioValue = request.POST.get('ratioValue')
    if wordCount:
        wordCount = int(wordCount)
    if ratioValue:
        ratioValue = int(ratioValue)/100
    sentenceCount = request.POST.get('sentenceCount')
    print(sentenceCount)
    summary=""

    

    if isURL(base_url):
        text = text_extractor(base_url)
    else:
        text =  wikipedia.page(base_url).content    

    if option==1:
        summary = summary_by_wordcount(text,wordCount)
    elif option==2:
        summary = summary_by_ratio(text,ratioValue)
    elif option==3:
        summary = LSA_summarizer(text,sentenceCount)
    elif option==4:
        summary = transformers_t5_base(text)
    elif option==5:
        summary = gpt2_summary(text)
    elif option==6:
        summary = bart(text)
    
    # extract_images(base_url)
    summary = clean_text(summary) 
    context = {'summary' : summary,'url' : base_url}
    return render(request,'output.html',context)

import re
def clean_text(text):  
    text = re.sub(r'\[.*?\]+', '', text)
    text1 = text.replace('\n', '')
    return text1
    

 