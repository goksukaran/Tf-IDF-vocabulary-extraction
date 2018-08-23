'''
Created on 15 Jul 2018

@author: goksukara
'''
from tfidf import TfIdf

def addallfilesinpath(path):
    pass

if __name__ == "__main__":
    
    Tf_idf = TfIdf('s')
    list=[['human', 'interface', 'computer'],['ship', 'interface', 'interface']]
    list1=[['ship', 'interface', 'interface']]
    list2=[['human', 'human', 'am']]
    #map(unicode,list)
    Tf_idf.add_document(list)
    Tf_idf.add_document(list1)
    Tf_idf.add_document(list2)
    Tf_idf.SaveCorpusdic()
    Tf_idf.loaddictionary()
    Tf_idf.buildmodel()
    Tf_idf.Saverelatedwords()
    Tf_idf.getTF_IDF()
    print(Tf_idf.listnhighIdfs(4))