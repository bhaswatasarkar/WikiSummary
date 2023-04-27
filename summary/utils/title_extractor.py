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


def title_extractor(base_url):
    '''
    Make the request
    ''' 
    r = requests.get(base_url)
    '''
    Extract HTML from Response object and print
    '''
    html = r.text
    ''' Create a BeautifulSoup object from the HTML
    '''
    soup = BeautifulSoup(html, "html.parser")
   

    title = str(soup.title)
    return title