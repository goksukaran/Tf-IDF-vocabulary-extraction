'''
Created on 21 Jun 2018

@author: goksukara
'''

import os.path



from TwitterPreprocessing import ReadData,TwitterData_Cleansing,TwitterCleanuper,TwitterData_TokenStem,RemoveStopwords,SaveTxt,Insert2corpus

from IntegrationTwitterprepocessing import Intergrationpreprocessing


# plotly configuration
#plotly.offline.init_notebook_mode()


def SearchSingleHastagtoTxt(queryhastag,workingdic):
    #To find absulet path
    os.chdir(workingdic)
    #parrentdirectory = os.path.abspath('..')
    #directoryfile=parrentdirectory+queryhastagå
    data = ReadData()
    data.readdata(workingdic+"/"+queryhastag)
    #print(data.processed_data.head(10))
    
    
    
    data = TwitterData_Cleansing(data)
    data.removesame()
    data.lowercase()
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
    data.save(queryhastag,workingdic)
    
#workingdic="/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Preprocessing/Data/Twitter/Raw"
#SearchSingleHastagtoTxt("#buildingautomation.csv",workingdic)

def inserttweets2corpus(filename,workingdic,output):
    os.chdir(workingdic)
    data = ReadData()
    data.readdata(workingdic+"/"+filename)
    
    data = TwitterData_Cleansing(data)
    data.removesame()
    data.lowercase()
    print(data.processed_data)
    data.cleanup(TwitterCleanuper())
    print(data.processed_data)
    data=Insert2corpus(data)
    data.insert(filename,output)
    
    
def integrationTweets(dataframe):
    data=Intergrationpreprocessing(dataframe)
    data.removesame()
    data.lowercase()
    return data.returnstring()   