from tfidf import TfIdf
import pandas as pd
def convert_stringto_unicode(string):
    list=string.split()
    pass
if __name__ == "__main__":
    corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Preprocessing/OwnDevelopment/Integration/' 
    filename='corpus_preprocessed'
    Tf_idf = TfIdf()
    for chunck_df in pd.read_csv(corpuspath+filename+'.csv',dtype={'file_name': str,"text": str}, chunksize=3,header=0,index_col=False,sep='\t',encoding='utf-8'):
        for index, row, in chunck_df.iterrows():  
            print(row['text'])
            row['text']=convert_stringto_unicode(row['text'])
            Tf_idf.add_document(row['file_name'],row['text'])
            