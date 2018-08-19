'''
Created on 17 Aug 2018

@author: goksukara
'''
import os
import glob
import pandas as pd
from PreprocessingTwitterApi import integrationTweets
def Addtweet2corpus():
    corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/corpus.csv'
    rootdir = '/Data/Twitter/Raw'
    outputdic='corpus.csv'
    extensions = ('*.csv')
    parrentdirectory = os.path.abspath('..')
    
    workingdic=parrentdirectory+rootdir
    os.chdir(parrentdirectory+rootdir)
    
    
    for filename in glob.glob(extensions):
        #filenamelist.append(file)
        #print(filename)
        dataframe=pd.read_csv(filename,names=["text"],dtype={"text":str})
        
        onelinetext=integrationTweets(dataframe)
        #print(onelinetext)
        raw_data =[[filename.encode("utf-8"),onelinetext.encode("utf-8")]]
    #print(text.encode("utf-8"))
        df = pd.DataFrame(raw_data,index=None)
        #print(df.to_string(index=False))
        with open(corpuspath, 'a') as outfile:
            df.to_csv(outfile,sep='\t',index=False,header=None, encoding="utf-8")
        
    
    
Addtweet2corpus()