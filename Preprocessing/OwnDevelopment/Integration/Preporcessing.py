'''
Created on 6 Aug 2018

@author: goksukara
'''
import pandas as pd
from PreprocessingClass import PreprocessingFunctions,Cleanupper
import sys
import os
sys.path.append('/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/TF-IDF')
#os.chdir('/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/TF-IDF/')
from tfidf import TfIdf



corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/'

cwd = os.getcwd()



filename='Building_automation'
Tf_idf = TfIdf(corpuspath+'Gensim_output')

for chunck_df in pd.read_csv(corpuspath+filename+'.csv', chunksize=5,header=0,index_col=False,sep='\t',encoding='utf-8'):
        
    dataprocesing=PreprocessingFunctions(chunck_df)
    Tokinzedsentece=dataprocesing.IterateoverRow()
    #print(Tokinzedsentece)
    #print('hi')
    Tf_idf.add_document(Tokinzedsentece)
    Tf_idf.Saverelatedwords()
        
        #dataprocesing.save(filename+'_preprocessed.csv')
filename='General'         
for chunck_df in pd.read_csv(corpuspath+filename+'.csv', chunksize=5,header=0,index_col=False,sep='\t',encoding='utf-8'):
    
    dataprocesing=PreprocessingFunctions(chunck_df)
    Tokinzedsentece=dataprocesing.IterateoverRow()
        
    Tf_idf.add_document(Tokinzedsentece)
    
   
Tf_idf.SaveCorpusdic()