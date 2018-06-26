'''
Created on 26 Jun 2018

@author: goksukara
'''
import collections
import math
import pandas as pd
import os
import sys
import argparse
import random
from tempfile import gettempdir
import zipfile
import csv

import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

from tensorflow.contrib.tensorboard.plugins import projector

class TwitterWod2vec():
    

    def TensorboardSummary_create_dic(self):
        current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--log_dir',
            type=str,
            default=os.path.join(current_path, 'log'),
            help='The log directory for TensorBoard summaries.')
        FLAGS, unparsed = parser.parse_known_args()
        
        # Create the directory for TensorBoard variables if there is not.
        if not os.path.exists(FLAGS.log_dir):
          os.makedirs(FLAGS.log_dir)
          
        print(FLAGS.log_dir)
    
    def read_data(self,filename):
        rootdir = '/OwnDevelopment/Data/Raw/'
        parrentdirectory = os.path.abspath('..')
        
        workingdic=parrentdirectory+rootdir
        os.chdir(parrentdirectory+rootdir)
        print(workingdic)

        reader = pd.read_csv(workingdic+filename)
              
        your_list = reader.values.T.tolist()
         
        return your_list
    def build_dataset(words, n_words):
      """Process raw inputs into a dataset."""
      count = [['UNK', -1]]
      count.extend(collections.Counter(words).most_common(n_words - 1))
      dictionary = dict()
      for word, _ in count:
        dictionary[word] = len(dictionary)
      data = list()
      unk_count = 0
      for word in words:
        index = dictionary.get(word, 0)
        if index == 0:  # dictionary['UNK']
          unk_count += 1
        data.append(index)
      count[0][1] = unk_count
      reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
      return data, count, dictionary, reversed_dictionary