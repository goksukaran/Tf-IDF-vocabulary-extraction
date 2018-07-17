
"""
Extract PDF text using PDFMiner. Adapted from
http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
"""
from pdf2text import pdf_to_text
from Preprocessing import Preprocessing
import codecs
#===============================================================================
# text=pdf_to_text('/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/ExampleProjects/Pdfparser/pdfrw/Pdfs/BuildingautomationsystemsConceptsandtechnologyreview.pdf')
# 
# processing=Preprocessing(text)
# 
# print(processing.processedtext)
# file=codecs.open('testfile.txt', 'w', encoding='utf8')
# file.write(text)
#===============================================================================

def extractpdf(filename):
    text=pdf_to_text(filename)