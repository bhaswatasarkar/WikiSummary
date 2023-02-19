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

from transformers import GPT2Tokenizer,GPT2LMHeadModel
from .text_extractor import *

def gpt2_summary(text):
    tokenizer=GPT2Tokenizer.from_pretrained('gpt2')
    model=GPT2LMHeadModel.from_pretrained('gpt2')
    inputs=tokenizer.batch_encode_plus([text],return_tensors='pt',max_length=1024)
    summary_ids=model.generate(inputs['input_ids'],early_stopping=True)
    GPT_summary=tokenizer.decode(summary_ids[0],skip_special_tokens=True)
    return GPT_summary