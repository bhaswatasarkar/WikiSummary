from django.shortcuts import render
from django.http import HttpResponse
from .algorihms.bart import *
from .algorihms.sumy import *
# from .algorihms.gensim import *
from .algorihms.gpt2 import *
from .algorihms.transformer import *
from .queryvalidator.queryvalidator import *
def homePage(request):
    return render(request,'home.html')

def outputPage(request):
    # base_url = "https://en.wikipedia.org/wiki/History_of_India"
    base_url = request.POST.get('url')
    option = int(request.POST.get('radio'))
    sentenceCount = request.POST.get('sentenceCount')
    print(sentenceCount)
    summary=""

    text = text_extractor(base_url)

    queryvalidator(base_url)


    if option==1:
        summary=""
    #     summary = summary_by_wordcount(base_url)
    # elif option==2:
    #     summary = summary_by_ratio(base_url)
    elif option==3:
        summary = LSA_summarizer(text,sentenceCount)
    elif option==4:
        summary = transformers_t5_base(text)
    elif option==5:
        summary = gpt2_summary(text)
    elif option==6:
        summary = bart(text)
        
    summary = clean_text(summary) 
    context = {'summary' : summary,'url' : base_url}
    return render(request,'output.html',context)

import re
def clean_text(text):  
    text = re.sub(r'\[.*?\]+', '', text)
    text1 = text.replace('\n', '')
    return text1
    

 