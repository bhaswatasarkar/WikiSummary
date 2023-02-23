import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
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
import torch
from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration


def transformers_t5_base(text):
    tokenizer = AutoTokenizer.from_pretrained('t5-base')
    model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)
    inputs = tokenizer.encode("summarize: " + text,
    return_tensors='pt',
    max_length=512,
    truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=80, length_penalty=5., num_beams=2)
    summary = tokenizer.decode(summary_ids[0])
    return summary

def transformers_t5_small(text):
    tokenizer1 = AutoTokenizer.from_pretrained('t5-small')
    my_model = T5ForConditionalGeneration.from_pretrained('t5-small')
    input_ids = tokenizer1.encode(text, return_tensors='pt', max_length=700,truncation=True)
    summary_ids = my_model.generate(input_ids,max_length=1000, min_length=500, length_penalty=5., num_beams=2)
    t5_summary = tokenizer1.decode(summary_ids[0])
    return t5_summary