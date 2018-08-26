'''
Created on 26 Jul 2018

@author: goksukara
'''
#!/usr/bin/env python
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
import json
import bz2
from numpy import record
import pandas as pd
baseurl='http://export.arxiv.org/oai2?'
corpuspath='/Users/goksukara/Desktop/Projects/EclipseWorkspace/Specilization/PhytonCode/Data/corpus.csv'
if __name__ == "__main__":
   
    url = baseurl
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)
    client = Client(url, registry)
    record = client.listSets()
    for word in record:
        print(word)
    #Write to file
    #with bz2.BZ2File('out.json', 'wb') as outfile:
    
for record in client.listRecords(metadataPrefix='oai_dc',set='cs'):
    header, metadata, _ = record
    doc = {}
    #Extract identifier
    doc["id"] = header.identifier()
    #Extract title and other metadata
    doc["title"] = "\n".join(metadata["title"])
    doc["abstract"] = "\n".join(metadata["description"])
    doc["authors"] = metadata["creator"]
    
    raw_data =[[doc["id"],doc["abstract"].encode("utf-8")]]

    df = pd.DataFrame(raw_data,index=None)
    #print(df.to_string(index=False))
    with open(corpuspath, 'a') as outfile:
        df.to_csv(outfile,sep='\t',index=False,header=None, encoding="utf-8")
    print("Wrote %s" % doc["abstract"])
