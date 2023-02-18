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
from collections.abc import Mapping
import nltk.data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
import torch
from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig
from transformers import pipeline

from .text_extractor import *

def bart(base_url):
    text = text_extractor(base_url)
    tokenizer=BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model=BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    inputs = tokenizer.encode(text,
    return_tensors='pt',
    max_length=1024,
    truncation=True)
    summary_ids = model.generate(inputs, max_length=1024, min_length=80, length_penalty=5., num_beams=2)
    bart_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return bart_summary
