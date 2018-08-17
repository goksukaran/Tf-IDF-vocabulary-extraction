'''
Created on 17 Aug 2018

@author: goksukara
'''
import pandas as pd

class Intergrationpreprocessing():
    processed_data=''
    retunString='a'
    def __init__(self, dataframe):
        self.processed_data=dataframe
        #print(self.dataframe)
    def removesame(self):
        self.processed_data=self.processed_data.drop_duplicates(subset=None, keep="first", inplace=False)    
    def IterateoverRow(self):
        self.retunString=''
        for index, row, in self.processed_data.iterrows():  
           
    
            self.retunString+=row['text']+'.'
    def lowercase(self):
        def makelower(row):
            row["text"]=row["text"].lower()
            #print(row["text"].lower())
            return row

        self.processed_data = self.processed_data.apply(makelower,axis=1)      
    def cleanup(self, cleanuper):
        t=self.processed_data
        for cleanup_method in cleanuper.iterate():
            t = cleanup_method(t)
        
        self.processed_data = t    
        
    def returnstring (self):
        return self.retunString
