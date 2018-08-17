'''
Created on 17 Aug 2018

@author: goksukara
'''
import os
import glob
import pandas as pd
from PreprocessingTwitterApi import integrationTweets
def Addtweet2corpus():
    rootdir = '/Data/Twitter/Raw'
    outputdic='corpus.csv'
    extensions = ('*.csv')
    parrentdirectory = os.path.abspath('..')
    
    workingdic=parrentdirectory+rootdir
    os.chdir(parrentdirectory+rootdir)
    
    
    for filename in glob.glob(extensions):
        #filenamelist.append(file)
        #print(filename)
        dataframe=pd.read_csv(filename)
        
        onelinetext=integrationTweets(dataframe)
        print(onelinetext)
    
    
Addtweet2corpus()