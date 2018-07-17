'''
Created on 15 Jul 2018

@author: goksukara
'''
from tfidf import TfIdf



if __name__ == "__main__":
    
    Tf_idf = TfIdf()
    list=[['human', 'interface', 'computer']]
    #map(unicode,list)
    Tf_idf.add_document("foo",list )
    Tf_idf.add_document("foo",list )
    Tf_idf.buildmodel()
    Tf_idf.Saverelatedwords()
    