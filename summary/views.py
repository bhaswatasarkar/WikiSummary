from django.shortcuts import render
from django.http import HttpResponse

from .algorihms.bart import *
from .algorihms.sumy import *
from .algorihms.gensim import *
from .algorihms.gpt2 import *
from .algorihms.transformer import *

from .utils.query_validator import *
from .utils.text_extractor import *
from .utils.title_extractor import *
from .utils.extract_image import *
from .utils.clean_elements import *
from .utils.filter_punctuations import *
from .utils.get_graph import *

import wikipedia

def homePage(request):
    return render(request,'home.html')

def outputPage(request):
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
    title=""
    url=""
    
    wordCount = 200
    if isURL(base_url):
        text = text_extractor(base_url)
        title = title_extractor(base_url)
        url = base_url
    else:
        url = wikipedia.page(base_url,auto_suggest=False).url
        text = text_extractor(url)
        title = title_extractor(url)
        

    if option==1:
        summary = summary_by_wordcount(text,wordCount)
    elif option==2:
        summary = summary_by_ratio(text,ratioValue)
    elif option==3:
        summary = LSA_summarizer(text,sentenceCount)
    elif option==4:
        summary = transformers_t5_small(text)
    elif option==5:
        summary = gpt2_summary(text)
    elif option==6:
        summary = bart(text)
    
    image = extract_image(url)
    summary = clean_summary(summary)
    title = clean_title(title)
    
    filtered_summary = filter_punctuations(summary)
    wordcloud = get_wordcloudplot(filtered_summary)
    wordcount = get_wordcountplot(filtered_summary)

   
    summary = summary.capitalize()
    # print(summary)

    context = {'summary' : summary, 'url' : base_url, 'title' : title, 'image' : image, 'wordcloud' : wordcloud, 'wordcount': wordcount}
    
    return render(request,'output.html',context)


def analysisPage(request):
    return render(request,'analysis.html')

def getAnalysisPage(request):
    base_url = request.POST.get('url')
    print(base_url)
    if(base_url == ""): 
        return render(request,'analysis.html')
    text=""
    url=""
    print(base_url)
    if isURL(base_url):
        text = text_extractor(base_url)
        title = title_extractor(base_url)
        url = base_url
    else:
        url = wikipedia.page(base_url,auto_suggest=False).url
        text = text_extractor(url)
        title = title_extractor(url)

    dataset = return_dataset(text)[0]
    dataword = return_dataset(text)[1]
    venn1 = get_venn_word_abstract(text,dataset)
    venn2 = get_venn_word_simple(text,dataset)
    venn3 = get_venn_count_abstract(text,dataset)
    venn4 = get_venn_count_simple(text,dataset)
    venn5 = get_venn_fullcount(text,dataset)
    wordcloud = get_wordcloud(dataset,dataword)
    context = {"venn1":venn1,"venn2":venn2,"venn3":venn3,"venn4":venn4,"venn5":venn5,"wordcloud":wordcloud}
    return render(request,'analysis.html',context)





 