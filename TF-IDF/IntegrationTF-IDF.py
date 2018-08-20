from tfidf import TfIdf
import pandas as pd
corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/'

if __name__ == "__main__":
   Tf_idf = TfIdf(corpuspath+'Gensim_output')
   Tf_idf.load()
   Tf_idf.buildmodel()
   Tf_idf.saveModel()
   #print(Tf_idf.corpus_dict)
   Tf_idf.listnhighIdfs(100)