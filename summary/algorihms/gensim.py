from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


def summary_by_ratio(text,ratioValue):
    # Summary by 0.1% of the original content
    summary_ratio = summarize(text, ratio = ratioValue) 
    return summary_ratio

def summary_by_wordcount(text,wordCount):
    summary_wordcount = summarize(text, word_count = wordCount)
    return summary_wordcount