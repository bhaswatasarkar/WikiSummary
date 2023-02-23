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


def text_extractor(base_url):
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
    '''
    Get the text out of the soup and print it
    '''
    ##text = soup.get_text()


    # Extract the plain text content from paragraphs
    paras = []
    for paragraph in soup.find_all('p'):
        paras.append(str(paragraph.text))

    # Extract text from paragraph headers
    heads = []
    for head in soup.find_all('span', attrs={'mw-headline'}):
        heads.append(str(head.text))

    # Interleave paragraphs & headers
    text = [val for pair in zip(paras, heads) for val in pair]
    text = ' '.join(text)
    return text