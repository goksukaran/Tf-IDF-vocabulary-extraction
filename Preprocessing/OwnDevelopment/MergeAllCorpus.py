'''
Created on 22 Jun 2018

@author: goksukara
'''
import glob, os.path
from PreprocessingTwitterApi import SearchSingleHastagtoTxt
def SeriesConversion():
    rootdir = '/Data/Twitter/Raw/'
    extensions = ('*.csv')
    parrentdirectory = os.path.abspath('..')
    
    workingdic=parrentdirectory+rootdir
    os.chdir(parrentdirectory+rootdir)
    print(workingdic)
    
    
    filenamelist =[]
    
    for file in glob.glob(extensions):
        filenamelist.append(file)
        
        
    
    
    for i in filenamelist:
        print(i)
        SearchSingleHastagtoTxt(i,workingdic)

def CombineAll():
    