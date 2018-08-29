'''
Created on 15 Jul 2018

@author: goksukara
'''
from tfidf import TfIdf

def addallfilesinpath(path):
    pass

if __name__ == "__main__":
    
    Tf_idf = TfIdf('s')
    list=[['human', 'human', 'interface'],['ship', 'human', 'interface']]
    list1=[['ship', 'humasn', 'interface']]
    list2=[['human', 'human', 'am']]
    list3=[['humafn', 'humasn', 'am1']]
    #map(unicode,list)
     
    Tf_idf.add_document(list)
    Tf_idf.add_document(list1)
    Tf_idf.Saverelatedwords()
    Tf_idf.add_document(list2)
    Tf_idf.add_document(list3)
    Tf_idf.SaveCorpusdic()
    Tf_idf.loaddictionary()
    Tf_idf.buildmodel()
    #Tf_idf.listnhighIdfs(10)
    Tf_idf.getTF_IDF()
     
   
