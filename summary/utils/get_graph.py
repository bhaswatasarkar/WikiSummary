import base64
from io import BytesIO
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
from wordcloud import WordCloud, STOPWORDS
from collections import Counter, OrderedDict
import operator
from matplotlib import rcParams
import matplotlib.cm as cm
import numpy as np
from ..algorihms.bart import *
from ..algorihms.sumy import *
from ..algorihms.gensim import *
from ..algorihms.gpt2 import *
from ..algorihms.transformer import *
from .clean_elements import *

from wordcloud import WordCloud
from matplotlib_venn import venn3
from matplotlib_venn import venn2
from matplotlib_venn_wordcloud import venn2_wordcloud
from matplotlib_venn_wordcloud import venn3_wordcloud
from geneview import generate_petal_labels
from geneview import venn

def get_wordset(summary):
    stopwords = STOPWORDS
    filtered_words = [word for word in summary.split() if word not in stopwords]
    counted_words = Counter(filtered_words)
    words = []
    counts = []
    for letter, count in counted_words.most_common(24):
        words.append(letter)
        counts.append(count)
    return words,counts

def return_dataset(text):
    dataset = []
    dataword = []
    words1 = get_wordset(clean_summary(LSA_summarizer(text,10)))[0]
    words2 = get_wordset(clean_summary(summary_by_wordcount(text,100)))[0]
    words3 = get_wordset(clean_summary(transformers_t5_small(text)))[0]
    words4 = get_wordset(clean_summary(gpt2_summary(text)))[0]
    words5 = get_wordset(clean_summary(bart(text)))[0]

    dataword.append(words1)
    dataword.append(words2)
    dataword.append(words3)
    dataword.append(words4)
    dataword.append(words5)

    dataset.append(set(words1))
    dataset.append(set(words2))
    dataset.append(set(words3))
    dataset.append(set(words4))
    dataset.append(set(words5))

    return dataset,dataword


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_wordcloudplot(summary):
    plt.switch_backend('AGG')
    stopwords = STOPWORDS
    word_cloud = WordCloud(stopwords=stopwords,collocations = False, background_color = 'white').generate(summary)
    rcParams['figure.figsize'] = 10, 20
    plt.figure(figsize=(10,5))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Wordcloud')
    graph = get_graph() 
    return graph

def get_wordcountplot(summary):
    plt.switch_backend('AGG')
    # stopwords = STOPWORDS
    # filtered_words = [word for word in summary.split() if word not in stopwords]
    # counted_words = Counter(filtered_words)
    words,counts = get_wordset(summary)
    # for letter, count in counted_words.most_common(24):
    #     words.append(letter)
    #     counts.append(count)
    colors = cm.rainbow(np.linspace(0, 1, 10))
    rcParams['figure.figsize'] = 12, 10
    plt.title('Top words in the Summary vs their count')
    plt.xlabel('Count')
    plt.ylabel('Words')
    plt.barh(words, counts, color=colors)
    graph = get_graph() 
    return graph



def get_venn_word_abstract(text,dataset):
    set1=dataset[0]
    set2=dataset[1]
    set3=dataset[2]
    set4=dataset[3]
    set5=dataset[4]
    plt.switch_backend('AGG')
    
    # set3 = set(get_wordset(clean_summary(transformers_t5_small(text)))[0])
    # set4 = set(get_wordset(clean_summary(gpt2_summary(text)))[0])
    # set5 = set(get_wordset(clean_summary(bart(text)))[0])
    
    fig, ax = plt.subplots(figsize=(10,10))
    ax.set_title("T5 , GPT2 and BART", fontsize=20)
    venn = venn3_wordcloud([set3, set4, set5], ax=ax, set_labels=['T5', 'GPT2', 'BART'] , word_to_frequency= None)

    venn.get_patch_by_id('100').set_color('red')
    venn.get_patch_by_id('100').set_alpha(0.4)
    venn.get_patch_by_id('110').set_color('green')
    venn.get_patch_by_id('110').set_alpha(0.4)
    venn.get_patch_by_id('010').set_color('blue')
    venn.get_patch_by_id('010').set_alpha(0.4)
    venn.get_patch_by_id('101').set_color('pink')
    venn.get_patch_by_id('101').set_alpha(0.4)
    venn.get_patch_by_id('111').set_color('yellow')
    venn.get_patch_by_id('111').set_alpha(0.4)
    venn.get_patch_by_id('011').set_color('orange')
    venn.get_patch_by_id('011').set_alpha(0.4)
    venn.get_patch_by_id('001').set_color('purple')
    venn.get_patch_by_id('001').set_alpha(0.4)

    graph = get_graph() 
    return graph


def get_venn_word_simple(text,dataset):
    set1=dataset[0]
    set2=dataset[1]
    set3=dataset[2]
    set4=dataset[3]
    set5=dataset[4]
    plt.switch_backend('AGG')
    
    # set1 = set(get_wordset(clean_summary(LSA_summarizer(text,10)))[0])
    # set2 = set(get_wordset(clean_summary(summary_by_wordcount(text,100)))[0])
    
    
    fig, ax = plt.subplots(figsize=(10,10))
    ax.set_title("LSA and Gensym", fontsize=20)
    venn = venn2_wordcloud([set1, set2], ax=ax, set_labels=['LSA', 'Gensym'] , word_to_frequency= None)

    venn.get_patch_by_id('10').set_color('red')
    venn.get_patch_by_id('10').set_alpha(0.4)
    venn.get_patch_by_id('11').set_color('green')
    venn.get_patch_by_id('11').set_alpha(0.4)
    venn.get_patch_by_id('01').set_color('yellow')
    venn.get_patch_by_id('01').set_alpha(0.4)

    graph = get_graph() 
    return graph


def get_venn_count_abstract(text,dataset):
    set1=dataset[0]
    set2=dataset[1]
    set3=dataset[2]
    set4=dataset[3]
    set5=dataset[4]
    plt.switch_backend('AGG')
    # set3 = set(get_wordset(clean_summary(transformers_t5_small(text)))[0])
    # set4 = set(get_wordset(clean_summary(gpt2_summary(text)))[0])
    # set5 = set(get_wordset(clean_summary(bart(text)))[0])
    data = {
    "T5":  set3,
    "GPT2": set4,
    "BART": set5,   
    }
    ax = venn(data ,legend_loc="upper right", legend_use_petal_color=True)
    ax.set_title("T5,GPT and Bart with counts", fontsize=20)  
    graph = get_graph() 
    return graph

def get_venn_count_simple(text,dataset):
    set1=dataset[0]
    set2=dataset[1]
    set3=dataset[2]
    set4=dataset[3]
    set5=dataset[4]
    plt.switch_backend('AGG')
    # set1 = set(get_wordset(clean_summary(LSA_summarizer(text,10)))[0])
    # set2 = set(get_wordset(clean_summary(summary_by_wordcount(text,100)))[0])
    data = {
    "LSA":  set1,
    "Gensym": set2   
    }
    ax = venn(data ,legend_loc="upper right", legend_use_petal_color=True)
    ax.set_title("LSA and Gensym", fontsize=20)  
    graph = get_graph() 
    return graph

def get_venn_fullcount(text,dataset):
    set1=dataset[0]
    set2=dataset[1]
    set3=dataset[2]
    set4=dataset[3]
    set5=dataset[4]
    plt.switch_backend('AGG')
    # set1 = set(get_wordset(clean_summary(LSA_summarizer(text,10)))[0])
    # set2 = set(get_wordset(clean_summary(summary_by_wordcount(text,100)))[0])
    # set3 = set(get_wordset(clean_summary(transformers_t5_small(text)))[0])
    # set4 = set(get_wordset(clean_summary(gpt2_summary(text)))[0])
    # set5 = set(get_wordset(clean_summary(bart(text)))[0])
    data = {
    "LSA":  set1,
    "Gensym": set2,
    "T5":  set3,
    "GPT2": set4,
    "BART": set5,   
    }
    ax = venn(data ,legend_loc="upper right", legend_use_petal_color=True)
    ax.set_title("All 5 with counts", fontsize=20)  
    graph = get_graph() 
    return graph


def get_wordcloud(dataset,dataword):
    weightsdict = { 'words1': 1, 'words2': 1,'words3': 1,'words4': 1,'words5': 1 }

    words1 = dataword[0]
    words2 = dataword[1]
    words3 = dataword[2]
    words4 = dataword[3]
    words5 = dataword[4]

    set1=dataset[0]
    set2=dataset[1]
    set3=dataset[2]
    set4=dataset[3]
    set5=dataset[4]
    Set_UNI = set1 | set2 | set3 | set4 | set5
    words_result = []
    for s1 in Set_UNI:
        result=s1, weightsdict['words1']*words1.count(s1)+weightsdict['words2']*words2.count(s1)+weightsdict['words3']*words3.count(s1)+weightsdict['words4']*words4.count(s1)+weightsdict['words5']*words5.count(s1)
        words_result.append(result)
    df = pd.DataFrame(words_result, columns =['Word','Score'])
    data = dict(zip(df['Word'].tolist(), df['Score'].tolist()))
    wc = WordCloud(width=800, height=400, max_words=200).generate_from_frequencies(data)
    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Wordcloud")  
    graph = get_graph() 
    return graph

