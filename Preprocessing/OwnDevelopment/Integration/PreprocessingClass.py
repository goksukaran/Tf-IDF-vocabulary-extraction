'''
Created on 6 Aug 2018

@author: goksukara
'''
class PreprocessingFunctions():
    data = []
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
    def save(self):
        pass        
    
    
class Cleanupper():
    def iterate(self):
        for cleanup_method in [self.stopword_remove,
                               ]:
            yield cleanup_method
    @staticmethod
    def stopword_remove(tweets):
        #tweets.loc[:, "text"].replace(regexp, "", inplace=True)
        #print(tweets)
        return tweets

    def convert_lowercase(self):
        pass
        