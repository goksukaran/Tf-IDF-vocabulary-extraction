'''
Created on 21 Jun 2018

@author: goksukara
'''

import os.path
import csv


from TwitterPreprocessing import ReadData,TwitterData_Cleansing,TwitterCleanuper,TwitterData_TokenStem,RemoveStopwords

#To find absulet path
parrentdirectory = os.path.abspath('..')

# plotly configuration
#plotly.offline.init_notebook_mode()

data = ReadData()
data.readdata(parrentdirectory+"/Data/Twitter/#Hamburg.csv")
print(data.processed_data.head(10))



data = TwitterData_Cleansing(data)
data.cleanup(TwitterCleanuper())
print(data.processed_data.head(10))



data = TwitterData_TokenStem(data)
data.tokenize()
data.stem()
print(data.processed_data.head(7))
data.processed_data.to_csv('out2.csv')

data=RemoveStopwords(data)
data.remove("english")
print(data.processed_data.head(10))
data.processed_data.to_csv('out2.csv')
