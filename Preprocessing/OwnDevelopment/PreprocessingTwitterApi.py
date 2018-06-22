'''
Created on 21 Jun 2018

@author: goksukara
'''

import os.path
import csv


from TwitterPreprocessing import ReadData,TwitterData_Cleansing,TwitterCleanuper,TwitterData_TokenStem,RemoveStopwords,SaveTxt



# plotly configuration
#plotly.offline.init_notebook_mode()


def SearchSingleHastagtoTxt(queryhastag):
    #To find absulet path
    parrentdirectory = os.path.abspath('..')
    directoryfile=parrentdirectory+"/Data/Twitter/Raw/"+queryhastag
    
    data = ReadData()
    data.readdata(directoryfile+".csv")
    #print(data.processed_data.head(10))
    
    
    
    data = TwitterData_Cleansing(data)
    data.cleanup(TwitterCleanuper())
    #print(data.processed_data.head(10))
    
    
    
    data = TwitterData_TokenStem(data)
    data.tokenize()
    data.stem()
    #print(data.processed_data.head(7))
    
    
    data=RemoveStopwords(data)
    data.remove()
    #print(data.processed_data.head(10))
    
    data=SaveTxt(data)
    data.save(queryhastag)
    

SearchSingleHastagtoTxt("#buildingautomation")

