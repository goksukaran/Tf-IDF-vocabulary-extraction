'''
Created on 21 Jun 2018

@author: goksukara
'''
import pandas as pd
import re as regex
import nltk
import os.path

class ReadData():
    data = []
    processed_data = []
    def readdata(self,csv_file):
        self.data = pd.read_csv(csv_file,names=["text"],dtype={"text":"str"})
        
        self.processed_data = self.data
        self.wordlist = []


class TwitterData_Cleansing(ReadData):
    def __init__(self, previous):
        self.processed_data = previous.processed_data
        
    def cleanup(self, cleanuper):
        t = self.processed_data
        for cleanup_method in cleanuper.iterate():
            t = cleanup_method(t)

        self.processed_data = t    
        
class TwitterCleanuper:
    def iterate(self):
        for cleanup_method in [self.remove_urls,
                               self.remove_usernames,
                               self.remove_na,
                               self.remove_special_chars,
                               self.remove_retweets,
                               self.remove_numbers]:
            yield cleanup_method
    @staticmethod
    def remove_by_regex(tweets, regexp):
        tweets.loc[:, "text"].replace(regexp, "", inplace=True)
        return tweets

    def remove_urls(self, tweets):
        return TwitterCleanuper.remove_by_regex(tweets, regex.compile(r"http.?://[^\s]+[\s]?"))
    def remove_na(self, tweets):
        return tweets[tweets["text"] != "Not Available"]

    def remove_special_chars(self, tweets):  # it unrolls the hashtags to normal words
        for remove in map(lambda r: regex.compile(regex.escape(r)), [",", ":", "\"", "=", "&", ";", "%", "$",
                                                                     "@", "%", "^", "*", "(", ")", "{", "}",
                                                                     "[", "]", "|", "/", "\\", ">", "<", "-",
                                                                     "!", "?", ".", "'",
                                                                     "--", "---", "#"]):
            tweets.loc[:, "text"].replace(remove, "", inplace=True)
        return tweets

    def remove_usernames(self, tweets):
        return TwitterCleanuper.remove_by_regex(tweets, regex.compile(r"@[^\s]+[\s]?"))

    def remove_numbers(self, tweets):
        return TwitterCleanuper.remove_by_regex(tweets, regex.compile(r"\s?[0-9]+\.?[0-9]*"))
    def remove_retweets(self,tweets):
        for remove in map(lambda r: regex.compile(regex.escape(r)), ["RT"]):
            tweets.loc[:, "text"].replace(remove, "", inplace=True)
        return tweets
    
    
class TwitterData_TokenStem(TwitterData_Cleansing):
    def __init__(self, previous):
        self.processed_data = previous.processed_data
        
    def stem(self, stemmer=nltk.PorterStemmer()):
        def stem_and_join(row):
            row["text"] = list(map(lambda str: stemmer.stem(str.lower()), row["text"]))
            return row

        self.processed_data = self.processed_data.apply(stem_and_join, axis=1)

    def tokenize(self, tokenizer=nltk.word_tokenize):
        def tokenize_row(row):
            
            row["text"] = tokenizer(str(row["text"]))
            row["tokenized_text"] = [] + row["text"]
            return row

        self.processed_data = self.processed_data.apply(tokenize_row,axis=1)
    
    
class RemoveStopwords(TwitterData_TokenStem):
    
    def __init__(self, previous):
        self.processed_data = previous.processed_data
    def remove(self):
        stopwords=nltk.corpus.stopwords.words("english")
        englishwords= nltk.corpus.words.words()
        def removestopwords(row):
            for w in row["tokenized_text"]: 
                if w in stopwords:
                   
                    row["tokenized_text"].remove(w)
                    #self.processed_data.append(w)
            
            for w in row["tokenized_text"]: 
                if w not in englishwords:
                    
                    row["tokenized_text"].remove(w)
                    #self.processed_data.append(w)
            
            
            return row["tokenized_text"]
        
            
        self.processed_data = self.processed_data.apply(removestopwords,axis=1)

          
class SaveTxt(RemoveStopwords):
    def save(self,queryhastag,workingdic):
        os.chdir(workingdic)
        parrentdirectory = os.path.abspath('..')
        print(parrentdirectory)
        directoryfile=parrentdirectory+"/Preprocessed/"+queryhastag
        print(directoryfile)
        self.processed_data.to_csv(directoryfile,index=False)
       
