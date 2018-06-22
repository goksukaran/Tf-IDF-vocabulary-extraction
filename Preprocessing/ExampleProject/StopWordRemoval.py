'''
Created on 22 Jun 2018

@author: goksukara
'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
example_sent = "This are a sample sentence, showing off the stop words filtration."
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(example_sent)
 
#filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w in stop_words:
        word_tokens.remove(w)
        #filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)
print(stop_words)