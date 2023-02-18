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

from sumy.summarizers.lex_rank import LexRankSummarizer
from .text_extractor import text_extractor
def LSA_summarizer(base_url):
    
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
        lsa_summary1+=str(sentence) 

    return lsa_summary1


########################################################
def lsa_method(text):
  my_parser = PlaintextParser.from_string(text,Tokenizer('english'))

def LEXRANK_summarizer(base_url):
    
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
    lsa_summarizer=LsaSummarizer()
    lsa_summary= lsa_summarizer(my_parser.document,50)
    dp = []
    for i in lsa_summary:
        lp = str(i)
    dp.append(lp)
    final_sentence = ' '.join(dp)
    lex_rank_summarizer = LexRankSummarizer()
    lexrank_summary = lex_rank_summarizer(my_parser.document,sentences_count=30)
    lex_summary=""
    for sentence in lexrank_summary:
        lex_summary+=str(sentence)  
    return lex_summary