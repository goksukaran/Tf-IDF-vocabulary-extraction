'''
Created on 6 Aug 2018

@author: goksukara
'''

from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.utils import tokenize
from gensim.parsing.porter import PorterStemmer
import nltk 
import pandas as pd
import sys
import enchant
sys.path.append('/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/TF-IDF')

class PreprocessingFunctions():
    processed_data = []
    filenamecolumn=[]
    textcolumn=[]
    tf_idf=''
    def __init__(self, dataframe,tf_idf):
        self.processed_data = dataframe
        self.filenamecolumn=self.processed_data.loc[:,'file_name']
        self.textcolumn=self.processed_data.loc[:,'text']
        self.tf_idf=tf_idf
    def IterateoverRow(self):
        for index, row, in self.processed_data.iterrows():  
           
            row['text']=self.cleanup(Cleanupper(),row['text'])
            #print(row['text'])
            self.tf_idf.add_document(row['text'])
            
       
    def cleanup(self, cleanuper,row):
        #print(self.processed_data.loc[:,'text'])
        
        for cleanup_method in cleanuper.iterate():
            row = cleanup_method(row)
        #self.processed_data.loc[:,'text'] = t
        #print(row)
        return row
    def add_document_dic(self):
        pass
    def save(self,filename):
        with open(filename, 'a',) as outfile:
            self.processed_data.to_csv(outfile,index=False,sep='\t',header=None,encoding='utf-8')
           
       
    
    
    
class Cleanupper():
    global p
    p = PorterStemmer()
    global d
    d = enchant.Dict("en_US")
    def iterate(self):
        for cleanup_method in [self.stopword_remove,
                               self.convert_lowercase,
                               self.remove_non_english,
                               #self.porter_stemmer,
                               self.remove_numbers,
                               self.tokenize
                               ]:
            yield cleanup_method
    @staticmethod
    def stopword_remove(sentence):
        #print(sentence)
        sentence=remove_stopwords(sentence)
        return sentence

    def convert_lowercase(self,sentence):
        #print(sentence)
        sentence=sentence.lower()
        return sentence
    def porter_stemmer(self,sentence):
        #print(sentence)
        sentence=p.stem_sentence(sentence)
        return str(sentence)
    def remove_non_english(self,sentence):
        english_words = []
        for word in sentence.split():
            if d.check(word):
                english_words.append(word)
                
        return (" ".join(english_words))
    def remove_numbers(self,sentence):
        sentence=strip_numeric(sentence)
        return str(sentence)
    def tokenize(self,sentence):
        sentences = nltk.sent_tokenize(sentence)
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        #print(sentence)
        #sentence=list(tokenize(sentence))
        #print(sentence)
        return tokenized_sentences