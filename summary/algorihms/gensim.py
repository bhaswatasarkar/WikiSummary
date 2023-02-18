import gensim
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import wikipedia
import requests
import heapq
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import collections
import nltk.data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
from .text_extractor import *

def summary_by_ratio(base_url):
    text = text_extractor(base_url)
    # Summary by 0.1% of the original content
    summary_ratio = summarize(text, ratio = 0.1) 
    return summary_ratio

def summary_by_ratio(base_url):
    text = text_extractor(base_url)
    summary_wordcount = summarize(text, word_count = 1000)
    return summary_wordcount