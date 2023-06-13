from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

from sumy.summarizers.lex_rank import LexRankSummarizer

def LSA_summarizer(text,sentenceCount):
    
    my_parser = PlaintextParser.from_string(text,Tokenizer('english'))

    # creating the LSA summarizer with summary of n sentences
    lsa_summarizer=LsaSummarizer()
    lsa_summary= lsa_summarizer(my_parser.document,sentenceCount)
    lsa_summary1=""
    for sentence in lsa_summary:
        lsa_summary1+=str(sentence) 

    return lsa_summary1


########################################################
def lsa_method(text):
  my_parser = PlaintextParser.from_string(text,Tokenizer('english'))

def LEXRANK_summarizer(text,sentenceCount):
    
    my_parser = PlaintextParser.from_string(text,Tokenizer('english'))
    lsa_summarizer=LsaSummarizer()
    lsa_summary= lsa_summarizer(my_parser.document,50)
    dp = []
    for i in lsa_summary:
        lp = str(i)
    dp.append(lp)
    final_sentence = ' '.join(dp)
    lex_rank_summarizer = LexRankSummarizer()
    lexrank_summary = lex_rank_summarizer(my_parser.document,sentences_count=sentenceCount)
    lex_summary=""
    for sentence in lexrank_summary:
        lex_summary+=" "+str(sentence)  
    return lex_summary
    