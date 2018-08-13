'''
Created on 10 Jul 2018

@author: goksukara
'''

import gensim.models.keyedvectors as word2vec

model = word2vec.KeyedVectors.load("model")

print(model.most_similar(positive=['sensor'], topn=5))