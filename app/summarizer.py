from nltk import sent_tokenize, word_tokenize
#from nltk.corpus import stopwords
from string import punctuation
import numpy as np
import pandas as pd
import re
import os
import codecs
from sklearn import feature_extraction
#import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances_argmin_min
#import nltk
import stop_words
from stop_words import get_stop_words
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
def find_similarities(text,no):
    #tokenize sentences
    sentences = text
    stop_words = get_stop_words('english')
    #set stop words
    stops = list(set(stop_words)) + list(punctuation)
    
    #vectorize sentences and remove stop words
    vectorizer = TfidfVectorizer(stop_words = stops)
    #transform using TFIDF vectorizer
    trsfm=vectorizer.fit_transform(sentences)
    
    #creat df for input article
    text_df = pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(),index=sentences)
    
    #declare how many sentences to use in summary
    num_sentences = text_df.shape[0]
    num_summary_sentences = int(np.ceil(num_sentences**no))
        
    #find cosine similarity for all sentence pairs
    similarities = cosine_similarity(trsfm, trsfm)
    
    #create list to hold avg cosine similarities for each sentence
    avgs = []
    for i in similarities:
        avgs.append(i.mean())
     
    #find index values of the sentences to be used for summary
    top_idx = np.argsort(avgs)[-num_summary_sentences:]
    
    return top_idx

def build_summary(text,no):
    #find sentences to extract for summary
    sents_for_sum = find_similarities(text.split(". "),no)
    #sort the sentences
    sort = sorted(sents_for_sum)
    #display which sentences have been selected
    print(sort)
    
    sent_list = sent_tokenize(text)
    #print number of sentences in full article
    print(len(sent_list))
    
    
    #extract the selected sentences from the original text
    sents = []
    for i in sort:
        sents.append(sent_list[i].replace('\n', ''))
    
    #join sentences together for final output
    summary = ' '.join(sents)
    return summary

def numCaps(text):
    sentences = text.split(". ")
    relavent = []
    for sen in sentences:
        words = sen.split(" ")
        words = words[1:len(words)]
        for word in words:
            if (word.capitalize() == word):
                relavent.append(sen)
                break
            
    return(relavent)         