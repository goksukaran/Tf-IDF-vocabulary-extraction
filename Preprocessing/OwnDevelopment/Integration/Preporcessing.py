'''
Created on 6 Aug 2018

@author: goksukara
'''
import pandas as pd
from PreprocessingClass import PreprocessingFunctions,Cleanupper 

filename='corpus'
for chunck_df in pd.read_csv(filename+'.csv',dtype={'filename':'str',"text":"str"}, chunksize=2,header=0,index_col=0, sep='\t'):
    dataprocesing=PreprocessingFunctions(chunck_df)
    print(chunck_df.columns.values)
    #dataprocesing.cleanup(Cleanupper())
    print(dataprocesing.processed_data.columns.values)
    dataprocesing.save(filename+'_preprocessed.csv')
    