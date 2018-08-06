'''
Created on 6 Aug 2018

@author: goksukara
'''
import pandas as pd
from PreprocessingClass import PreprocessingFunctions,Cleanupper 

for chunck_df in pd.read_csv('Corpus_dic.csv',sep="\s+",header=['ID',"Text"],names=['ID',"Text"],dtype={"Text":"str"}, chunksize=1):
    dataprocesing=PreprocessingFunctions(chunck_df)
    dataprocesing.cleanup(Cleanupper())
    print(dataprocesing.processed_data.head(5))
    