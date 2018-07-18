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

class TfIdf():
    global filename
    filename="ad"
    def __init__(self):
        self.weighted = False
        self.spesificwords=corpora.Dictionary()
        self.raw_corpus = []
        self.corpus_dict = corpora.Dictionary()
        self.document_name=collections.OrderedDict()
        self.idf_results=collections.OrderedDict()
        self.tfidf=models.TfidfModel()
    def add_document(self,doc_name,text):
        self.corpus_dict.add_documents(text)
        self.corpus_dict.save('/tmp/'+filename+'.dict')
        #self.document_name.append(doc_name)
        #print([self.corpus_dict.doc2bow(t) for t in text])
        tmp=[self.corpus_dict.doc2bow(t) for t in text]
        self.raw_corpus.append(tmp[0])
        
        #print(self.raw_corpus)
        #print(self.spesificwords)
    def buildmodel(self):
        corpora.MmCorpus.serialize('/tmp/'+filename+'.mm', self.raw_corpus)
        #print(self.raw_corpus)
        self.corpus_dict = corpora.Dictionary.load('/tmp/'+filename+'.dict')
        corpus = corpora.MmCorpus('/tmp/'+filename+'.mm')
    
        self.tfidf = models.TfidfModel(corpus,normalize=True)
        self.idf_results=OrderedDict(sorted(self.tfidf.idfs.items(), key = itemgetter(1), reverse = True))
     
    def Saverelatedwords(self):
        self.spesificwords=self.corpus_dict
        #print(self.spesificwords)
    def listnhighIdfs(self,n):
        
        for words in list(self.idf_results.keys())[0:n]:
            print(words)
            print(self.corpus_dict[words])
        
        