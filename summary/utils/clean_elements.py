import re

def clean_summary(text):  
    text = re.sub(r'\[.*?\]+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = text.replace('\n', '')
    return text

def clean_title(text):
    text = text.replace('<title>','')
    text = text.replace('</title>','')
    text = text.replace('-','')
    text = text.replace('Wikipedia','')
    text = text.strip() 
    return text