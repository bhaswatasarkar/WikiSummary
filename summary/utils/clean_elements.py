import re
import nltk.data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
# nltk.download('punkt')
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
sw_nltk = stopwords.words('english')
import string

def clean_summary(text): 
    stoplist = set(stopwords.words("english")) 
    # text = re.sub(r'\[.*?\]+', '', text)
    # text = re.sub(r'<.*?>', '', text)
    # text = text.replace('\n', '')
    text = text.translate(str.maketrans('', '', string.punctuation))

    text=re.sub(r'\w*\d\w*', '', text).strip()
    text = [word for word in text.split() if word.lower() not in sw_nltk]
    text = " ".join(text)
    text = [word for word in text.split() if word not in stoplist]
    text = " ".join(text)
    text = re.sub(r'(?:^| )\w(?:$| )', ' ', text).strip()
    return text

def clean_title(text):
    text = text.replace('<title>','')
    text = text.replace('</title>','')
    text = text.replace('-','')
    text = text.replace('Wikipedia','')
    text = text.strip() 
    return text

def clean_summary_homepage(text):
    text = re.sub(r'\[.*?\]+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = text.replace('\n', '')
    return text