
"""
Extract PDF text using PDFMiner. Adapted from
http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
"""
from pdf2text import pdf_to_text
import codecs
import glob, os.path
import pandas as pd
import numpy as np
from gensim.parsing.preprocessing import strip_multiple_whitespaces
#===============================================================================
# text=pdf_to_text('/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/ExampleProjects/Pdfparser/pdfrw/Pdfs/BuildingautomationsystemsConceptsandtechnologyreview.pdf')
# 
# processing=Preprocessing(text)
# 
# print(processing.processedtext)
# file=codecs.open('testfile.txt', 'w', encoding='utf8')
# file.write(text)
#===============================================================================
corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/corpus.csv'
pdfpath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/PdfParser/Pdfs'

def extractpdf(filename):
    text=pdf_to_text(filename)
    return text
    
def save(filename,text):
    
    raw_data =[[filename,text.encode("utf-8")]]
    #print(text.encode("utf-8"))
    df = pd.DataFrame(raw_data,columns=['Filename','Text'],index=None)
    print(df.to_string(index=False))
    with open(corpuspath, 'a') as outfile:
        df.to_csv(outfile,sep='\t',index=False,header=None)
        
    
        
    
class Preprocessing():
    processedtext=""
    def __init__(self, text):
        self.processedtext = text
        
    def Removenewlines(self):
        self.processedtext=strip_multiple_whitespaces(self.processedtext)

        print(self.processedtext)
    def save(self,filename):
        raw_data =[[filename,self.processedtext.encode("utf-8")]]
        #print(text.encode("utf-8"))
        df = pd.DataFrame(raw_data,columns=['Filename','Text'],index=None)
        print(df.to_string(index=False))
        with open(corpuspath, 'a') as outfile:
            df.to_csv(outfile,sep='\t',index=False,header=None)

  

        
if __name__ == "__main__":
    extensions = ('*.pdf')
    filenamelist =[]
    os.chdir(pdfpath)   
    for filename in glob.glob(extensions):
     
        #filenamelist.append(file)
        #print(filename)
        text=str(extractpdf(filename))
        
        prepocessing=Preprocessing(text)
        prepocessing.Removenewlines()
        prepocessing.save(filename)