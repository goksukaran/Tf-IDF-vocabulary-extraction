'''
Created on 12 Jul 2018

@author: goksukara
'''
from pdfrw import PdfReader
import os 
cwd = os.getcwd()

x = PdfReader(cwd+'/Pdfs/BuildingautomationsystemsConceptsandtechnologyreview.pdf')

print(x.pages[0].Annots[1])