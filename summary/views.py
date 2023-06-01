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
    
    
    if isURL(base_url):
        text = text_extractor(base_url)
        title = title_extractor(base_url)
        url = base_url
    else:
        url = wikipedia.page(base_url,auto_suggest=False).url
        text = text_extractor(url)
        title = title_extractor(url)
    
    # text = clean_rawtext(text)

    if option==1:
        summary = summary_by_wordcount(text,wordCount)
    elif option==2:
        summary = summary_by_ratio(text,ratioValue)
    elif option==3:
        summary = LSA_summarizer(text,sentenceCount)
    elif option==4:
        summary = transformer_t5(text)
    elif option==5:
        summary = gpt2_summary(text)
    elif option==6:
        summary = bart(text)
    
    image = extract_image(url)
    summary = clean_summary_homepage(summary)
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

    text = clean_rawtext(text)

    dataset = return_dataset(text)[0]
    dataword = return_dataset(text)[1]
    venn1 = get_venn_word_abstract(text,dataset)
    venn2 = get_venn_word_simple(text,dataset)
    venn3 = get_venn_count_abstract(text,dataset)
    venn4 = get_venn_count_simple(text,dataset)
    venn5 = get_venn_fullcount(text,dataset)
    wordcloud = get_wordcloud(dataset,dataword)

    context = {"venn1":venn1,"venn2":venn2,"venn3":venn3,"venn4":venn4,"venn5":venn5,"wordcloud":wordcloud}

    print_keywords(dataset)
    return render(request,'analysis.html',context)


def clean_rawtext(text):
    stoplist = set(stopwords.words("english"))
    text=re.sub(r'\w*\d\w*', '', text).strip()
    text = [word for word in text.split() if word.lower() not in sw_nltk]
    text = " ".join(text)
    text=[word for word in text.split() if word not in stoplist]
    text = " ".join(text)
    text=re.sub(r'(?:^| )\w(?:$| )', ' ', text).strip()
    return text

def print_keywords(dataset):
    LSA=dataset[0]
    Gensym=dataset[1]
    T5=dataset[2]
    GPT2=dataset[3]
    BART=dataset[4]

    S4_A = (LSA & Gensym) - T5 - GPT2 - BART #example: This represents words present in both LSA and Gensym totally excluding other sets
    S4_B = (LSA & T5) - Gensym - GPT2 - BART
    S4_C = (LSA & GPT2) - T5 - Gensym - BART
    S4_D = (LSA & BART) - T5 - Gensym - GPT2
    S4_E = (Gensym & T5) - LSA - GPT2 - BART
    S4_F = (Gensym & GPT2) - T5 - LSA - BART
    S4_G = (Gensym & BART) - T5 - GPT2 - LSA
    S4_H = (T5 & GPT2) - Gensym - LSA - BART
    S4_I = (T5 & BART) - Gensym - GPT2 - LSA
    S4_J = (GPT2 & BART) - T5 - Gensym - LSA
    print(S4_A)
    print("length : "+str(len(S4_A))+"\n\n")
    print(S4_B)
    print("length : "+str(len(S4_B))+"\n\n")
    print(S4_C)
    print("length : "+str(len(S4_C))+"\n\n")
    print(S4_D)
    print("length : "+str(len(S4_D))+"\n\n")
    print(S4_E)
    print("length : "+str(len(S4_E))+"\n\n")
    print(S4_F)
    print("length : "+str(len(S4_F))+"\n\n")
    print(S4_G)
    print("length : "+str(len(S4_G))+"\n\n")
    print(S4_H)
    print("length : "+str(len(S4_H))+"\n\n")
    print(S4_I)
    print("length : "+str(len(S4_I))+"\n\n")
    print(S4_J)
    print("length : "+str(len(S4_J))+"\n\n")


    # #########


    S5_A = (T5 & GPT2 & BART) - LSA - Gensym
    S5_B = (Gensym & GPT2 & BART) -LSA - T5
    S5_C = (T5 & Gensym & BART) - LSA - GPT2
    S5_D = (T5 & Gensym & GPT2) - LSA - BART
    S5_E = (LSA & GPT2 & BART) - Gensym - T5
    S5_F = (T5 & LSA & BART) - Gensym - GPT2
    S5_G = (T5 & GPT2 & LSA) - Gensym - BART
    S5_H = (Gensym & LSA & BART) - T5 - GPT2
    S5_I = (Gensym & GPT2 & LSA) - T5 - BART
    S5_J = (T5 & Gensym & LSA) - GPT2 - BART
    print(S5_A)
    print("length : "+str(len(S5_A))+"\n\n")
    print(S5_B)
    print("length : "+str(len(S5_B))+"\n\n")
    print(S5_C)
    print("length : "+str(len(S5_C))+"\n\n")
    print(S5_D)
    print("length : "+str(len(S5_D))+"\n\n")
    print(S5_E)
    print("length : "+str(len(S5_E))+"\n\n")
    print(S5_F)
    print("length : "+str(len(S5_F))+"\n\n")
    print(S5_G)
    print("length : "+str(len(S5_G))+"\n\n")
    print(S5_H)
    print("length : "+str(len(S5_H))+"\n\n")
    print(S5_I)
    print("length : "+str(len(S5_I))+"\n\n")
    print(S5_J)
    print("length : "+str(len(S5_J))+"\n\n")


    # #########


    S6_A = (T5 & GPT2 & BART & LSA) - Gensym
    S6_B = (T5 & GPT2 & BART & Gensym) - LSA
    S6_C = (T5 & GPT2 & Gensym & LSA) - BART
    S6_D = (T5 & Gensym & BART & LSA) - GPT2
    S6_E = (Gensym & GPT2 & BART & LSA) - T5

    print(S6_A)
    print("length : "+str(len(S6_A))+"\n\n")
    print(S6_B)
    print("length : "+str(len(S6_B))+"\n\n")
    print(S6_C)
    print("length : "+str(len(S6_C))+"\n\n")
    print(S6_D)
    print("length : "+str(len(S6_D))+"\n\n")
    print(S6_E)
    print("length : "+str(len(S6_E))+"\n\n")