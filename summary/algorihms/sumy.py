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
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


def func():
    base_url = "https://en.wikipedia.org/wiki/History_of_India"
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
    soup = BeautifulSoup(html, "lxml")
    '''
    Get the text out of the soup and print it
    '''
    #text1 = soup.get_text()


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
    my_parser = PlaintextParser.from_string(text,Tokenizer('english'))
    # creating the LSA summarizer with summary of 30 sentences
    lsa_summarizer=LsaSummarizer()
    lsa_summary= lsa_summarizer(my_parser.document,30)
    for sentence in lsa_summary:
        print(sentence)