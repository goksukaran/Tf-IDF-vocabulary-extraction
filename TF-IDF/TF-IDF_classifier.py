'''
Created on 15 Jul 2018

@author: goksukara
'''
from tfidf import TfIdf



if __name__ == "__main__":
    
    Tf_idf = TfIdf()
    list=[['human', 'interface', 'computer']]
    list1=[['ship', 'interface', 'interface']]
    list2=[['human', 'human', 'am']]
    #map(unicode,list)
    Tf_idf.add_document("foo",list)
    Tf_idf.add_document("foo",list1)
    Tf_idf.add_document("foo",list2)
    Tf_idf.buildmodel()
    Tf_idf.Saverelatedwords()
    print(Tf_idf.listnhighIdfs(4))