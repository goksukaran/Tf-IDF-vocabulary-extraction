'''
Created on 6 Aug 2018

@author: goksukara
'''
import pandas as pd
from PreprocessingClass import PreprocessingFunctions,Cleanupper 
corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/'

filename='corpus'
for chunck_df in pd.read_csv(corpuspath+filename+'.csv',dtype={'file_name':'str',"text":"str"}, chunksize=10,header=0,index_col=0, sep='\t'):
    dataprocesing=PreprocessingFunctions(chunck_df)
    print(dataprocesing.processed_data.loc[: , "text"])
    #dataprocesing.cleanup(Cleanupper())
    #print(dataprocesing.processed_data.columns.values)
    dataprocesing.save(filename+'_preprocessed.csv')
    