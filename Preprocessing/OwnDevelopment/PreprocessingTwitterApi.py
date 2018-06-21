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

#To find absulet path
parrentdirectory = os.path.abspath('..')

# plotly configuration
#plotly.offline.init_notebook_mode()

data = TwitterData_Initialize()
data.read(parrentdirectory+"/Data/Twitter/#Berlin.csv")
print(data.processed_data.head(10))