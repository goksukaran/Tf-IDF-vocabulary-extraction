'''
Created on 6 Aug 2018

@author: goksukara
'''
import pandas as pd
from PreprocessingClass import PreprocessingFunctions,Cleanupper 

for chunck_df in pd.read_csv('Corpus_dic.csv',dtype={"text":"str"}, chunksize=5):
    dataprocesing=PreprocessingFunctions(chunck_df)
    dataprocesing.cleanup(Cleanupper())
    #print(dataprocesing.data)
    