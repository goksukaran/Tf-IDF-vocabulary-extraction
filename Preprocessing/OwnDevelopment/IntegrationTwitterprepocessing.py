'''
Created on 17 Aug 2018

@author: goksukara
'''
import pandas as pd
class Intergrationpreprocessing():
    processed_data=''
    retunString=''
    def __init__(self, dataframe):
        self.processed_data=dataframe
        #print(self.dataframe)
    def removesame(self):
        self.processed_data=self.processed_data.drop_duplicates(subset=None, keep="first", inplace=False)    
    def lowercase(self):
        def makelower(row):
            row["text"]=row["text"].lower()
            print(row["text"].lower())
            return row
    def returnstring (self):
        return self.processed_data      