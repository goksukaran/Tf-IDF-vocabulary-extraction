import tweepy
import csv
import pandas as pd
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

try:
    import json
except ImportError:
    import simplejson as json

global hastaglist
def searchandsave(search_text):
    # Open/Create a file to append datan
    csvFile = open("data/"+search_text+'.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
   
    for tweet in tweepy.Cursor(api.search,q=search_text,count=1000000,
                               lang="en",
                               since="2000-04-03").items(1):
       print (tweet.created_at, tweet.text)
       csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    

 


def initilizeTweppy():
    consumer_key = 'T4S8NM1zImZaJrdh2eoojzEsK'
    consumer_secret = 'vLVD9nPSnLoxAgQonJZC7Mrp0GLliQFxcXg0d6nMP1b6DgXwum'
    access_token = '1004965282429980672-m3bviyqV4DigZz1mxubm8iH46sbpDn'
    access_secret = 'ZH41wTFQuYKYhP2oF8vIsbTz2AUpnD8ByaOBQ1E9bt2Um'  
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    #Connect Api
    global api 
    api = tweepy.API(auth)

    #Error handling
    if (not api):
        print ("Problem connecting to API")  
def Saveextracthastags():
    hastaglist=appen(tweet.entities.get('hashtags')[0]['text'])
def main():
  print("Hello World!")
  initilizeTweppy()
 # Saveextracthastags()
  searchandsave("#Berlin");
if __name__== "__main__":
  main()

