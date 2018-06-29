'''
Created on 22 Jun 2018

@author: goksukara
'''
import glob, os.path
import pandas as pd
import csv
from PreprocessingTwitterApi import SearchSingleHastagtoTxt
def SeriesConversion():
    rootdir = '/Data/Twitter/Raw/'
    extensions = ('*.csv')
    parrentdirectory = os.path.abspath('..')
    
    workingdic=parrentdirectory+rootdir
    os.chdir(parrentdirectory+rootdir)
    print(workingdic)
    
    
    filenamelist =[]
    
    for file in glob.glob(extensions):
        filenamelist.append(file)
        
        
    
    
    for i in filenamelist:
        print(i)
        SearchSingleHastagtoTxt(i,workingdic)

#SeriesConversion()
def CombineAll():
    Resultfilename="merged"
    
    rootdir = '/Data/Twitter/Preprocessed/'
    extensions = ('*.csv')
    parrentdirectory = os.path.abspath('..')
    
    workingdic=parrentdirectory+rootdir
    os.chdir(parrentdirectory+rootdir)
    print(workingdic)
    
    
    filenamelist =[]
    list_ = []
    
    for file in glob.glob(extensions):
        filenamelist.append(file)
    
    for file in filenamelist:
        print(file)
        df = pd.read_csv(file,index_col=None, header=0)
        list_.append(df)
    frame = pd.concat(list_)
    #===========================================================================
    # with open('merged.csv', "w",encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(frame)
    #===========================================================================
    
    frame.to_csv("merged.csv", sep='\t',index=False)
CombineAll()