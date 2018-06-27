'''
Created on 27 Jun 2018

@author: goksukara
'''

import os
import pandas as pd 

class GenisimRun():
    data=[]
    def DataRead(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        data=pd.read_csv(dir_path+"/Data/Raw/#IIoT.csv")
        return data