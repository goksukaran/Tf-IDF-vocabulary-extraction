'''
Created on 21 Aug 2018

@author: goksukara
'''
from tfidf import TfIdf
import pandas as pd
corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/'

if __name__ == "__main__":
   Tf_idf = TfIdf(corpuspath+'Gensim_output')
   Tf_idf.loaddictionary()
   Tf_idf.loadModel()
   #Tf_idf.getTF_IDF()
   #Tf_idf.buildmodel()
   #Tf_idf.saveModel()
   #print(Tf_idf.corpus_dict)
   Tf_idf.listnhighIdfs(100)