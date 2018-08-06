'''
Created on 6 Aug 2018

@author: goksukara
'''

from gensim.parsing.preprocessing import remove_stopwords
import pandas as pd
class PreprocessingFunctions():
    processed_data = []
    def __init__(self, dataframe):
        self.processed_data = dataframe
       
    def cleanup(self, cleanuper):
        t = self.processed_data
        for cleanup_method in cleanuper.iterate():
            t = cleanup_method(t)

        self.processed_data = t
    
    def tokenization(self):
        pass
    def add_document_dic(self):
        pass
    def save(self):
        with open('Preprocessed.csv', 'a') as outfile:
            self.processed_data.to_csv(outfile)
            #writer = csv.writer(outfile)
            #writer.writerow(self.processed_data)
       
    
    
    
class Cleanupper():
    def iterate(self):
        for cleanup_method in [self.stopword_remove,
                               ]:
            yield cleanup_method
    @staticmethod
    def stopword_remove(sentence):
        sentence=remove_stopwords(str(sentence))
        #print(sentence)
        return sentence

    def convert_lowercase(self):
        pass
        