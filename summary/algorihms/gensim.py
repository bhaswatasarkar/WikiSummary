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
from collections.abc import Mapping
import nltk.data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')


def summary_by_ratio(text,ratioValue):
    # Summary by 0.1% of the original content
    summary_ratio = summarize(text, ratio = ratioValue) 
    return summary_ratio

def summary_by_wordcount(text,wordCount):
    summary_wordcount = summarize(text, word_count = wordCount)
    return summary_wordcount