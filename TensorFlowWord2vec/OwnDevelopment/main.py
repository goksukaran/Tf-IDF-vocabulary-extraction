'''
Created on 26 Jun 2018

@author: goksukara
'''
from TwitterWord2vec import TwitterWod2vec

tensor=TwitterWod2vec()
tensor.TensorboardSummary_create_dic()


vocabulary=tensor.read_data("merged.csv")
print('Data size', vocabulary)
print(vocabulary)

#===============================================================================
# # Step 2: Build the dictionary and replace rare words with UNK token.
# vocabulary_size = 50000
# 
# data, count, dictionary, reverse_dictionary=tensor.build_dataset(vocabulary,
#                                                                   vocabulary_size)
# 
# del vocabulary  # Hint to reduce memory.
# print('Most common words (+UNK)', count[:5])
# print('Sample data', data[:10], [reverse_dictionary[i] for i in data[:10]])
# 
# data_index = 0
#===============================================================================