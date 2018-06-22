'''
Created on 21 Jun 2018

@author: goksukara
'''
from collections import Counter
import nltk
import pandas as pd
#from emoticons import EmoticonDetector
import re as regex
import numpy as np
import plotly
from plotly import graph_objs
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from time import time
import gensim
import os.path

from LoadData import TwitterData_Initialize
from TwitterCleanuper import TwitterData_Cleansing,TwitterCleanuper
from TokenizationStemming import TwitterData_TokenStem
from TwitterData_wordlist import TwitterData_Wordlist
# plotly configuration
#plotly.offline.init_notebook_mode()

#To find absulet path
parrentdirectory = os.path.abspath('..')


data = TwitterData_Initialize()
data.initialize(parrentdirectory+"/Data/EmotionsData/train.csv")
#print(data.processed_data.head(10))
data.processed_data.to_csv('first1.csv')

data = TwitterData_Cleansing(data)
data.cleanup(TwitterCleanuper())
#print(data.processed_data.head(5))
  
data.processed_data.to_csv('out.csv')  
data = TwitterData_TokenStem(data)
data.tokenize()
data.stem()
#print(data.processed_data.head(7))
data.processed_data.to_csv('Tokinezed.csv')
words = Counter()
for idx in data.processed_data.index:
    words.update(data.processed_data.loc[idx, "text"])
    
print(words.most_common(5))
    
stopwords=nltk.corpus.stopwords.words("english")
whitelist = ["n't", "not"]
for idx, stop_word in enumerate(stopwords):
    if stop_word not in whitelist:
        del words[stop_word]
print(words.most_common(5))
     
data = TwitterData_Wordlist(data)
data.build_wordlist()
