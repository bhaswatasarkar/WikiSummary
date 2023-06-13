import string
import re
import pandas as pd
import numpy as np
import collections
import nltk.data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
# nltk.download('punkt')
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
import matplotlib.pyplot as plt



def filter_punctuations(summary):
    sw_nltk = stopwords.words('english')
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in summary:
        if ele in punc:
            summary = summary.replace(ele, "")
    
    summary = summary.translate(str.maketrans('', '', string.punctuation))
    summary = re.sub(r'\w*\d\w*', '', summary).strip()
    summary = [word for word in summary.split() if word.lower() not in sw_nltk]
    summary = " ".join(summary)
    summary = re.sub(r'(?:^| )\w(?:$| )', ' ', summary).strip()
    summary = summary.replace("-","")
    return summary