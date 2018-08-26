#!/usr/bin/env python

"""The simplest TF-IDF library imaginable.

Add your documents as two-element lists `[docname,
[list_of_words_in_the_document]]` with `addDocument(docname, list_of_words)`.
Get a list of all the `[docname, similarity_score]` pairs relative to a
document by calling `similarities([list_of_words])`.

See the README for a usage example.

"""

import sys
import os
import collections
from gensim import corpora, models
from collections import OrderedDict
from operator import itemgetter  
import copy
class TfIdf():
    global filenamedic
    filename="ad"
    def __init__(self,filedic):
        self.weighted = False
        self.spesificwords=corpora.Dictionary()
        self.raw_corpus = []
        self.corpus_dict = corpora.Dictionary()
        self.document_name=collections.OrderedDict()
        self.idf_results=collections.OrderedDict()
        self.tfidf=models.TfidfModel()
        self.filedic=filedic
        self.corpus=''
        self.model_results=''
        self.tf_idf_results=dict()
    def add_document(self,text):
        self.corpus_dict.add_documents(text)
        print(len(self.raw_corpus))
        #self.document_name.append(doc_name)
        #print([self.corpus_dict.doc2bow(t) for t in text])
        tmp=[self.corpus_dict.doc2bow(t) for t in text]
        print(tmp)
        if tmp!=[]:
            self.raw_corpus.append(tmp[0])
        corpora.MmCorpus.serialize(self.filedic+'.mm', self.raw_corpus)
        #print(self.raw_corpus)
        #print(self.spesificwords)
    def loaddictionary(self):
        self.corpus_dict = corpora.Dictionary.load(self.filedic+'.dict')
        self.corpus = corpora.MmCorpus(self.filedic+'.mm')
        self.spesificwords=corpora.Dictionary.load(self.filedic+'spesific.dict')
        print(self.corpus)
    def buildmodel(self):
        #print(self.corpus)
        self.tfidf = models.TfidfModel(self.corpus,normalize=True)
        self.model_results=self.tfidf[self.corpus]
        self.idf_results=OrderedDict(sorted(self.tfidf.idfs.items(), key = itemgetter(1), reverse = True))
    
    def SaveCorpusdic(self):
        self.corpus_dict.save(self.filedic+'.dict')
        
        
    def Saverelatedwords(self):
        self.spesificwords=copy.copy(self.corpus_dict)
        self.spesificwords.save(self.filedic+'spesific.dict')
    def calculatesimpetfidf(self):
        pass
        
    def listnhighIdfs(self,n):
        self.idf_results=OrderedDict(sorted(self.tfidf.idfs.items(), key = itemgetter(1), reverse = True))
        print(self.tfidf.dfs.items())
        print(self.tfidf.idfs.items())
        
        for words in list(self.idf_results.keys())[0:n]:
            if words in (self.spesificwords):
                print(self.spesificwords[words])
    def loadModel(self):
        self.tfidf=models.TfidfModel.load(self.filedic+'TF_IDFmodel')  
        
    def saveModel(self):
        self.tfidf.save(self.filedic+'TF_IDFmodel')
    
    def printsome(self):
            
    
    def getTF_IDF(self):
        print(self.tf_idf_results)
        print(self.corpus_dict)
        for words in (self.spesificwords):
            print(words)
            print(self.tf_idf_results[words])
            #print(self.tf_idf_results[words])
        #=======================================================================
        # print(self.corpus_dict)
        # print(self.spesificwords)
        # print(len(self.tfidf.idfs.keys()))
        # for words in self.corpus_dict:
        #     print(self.corpus_dict[words])
        #     #print(words)
        #     pass
        #=======================================================================