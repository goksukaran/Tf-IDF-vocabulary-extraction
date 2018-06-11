import tweepy
import csv
import pandas as pd
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from pprint import pprint

try:
    import json
except ImportError:
    import simplejson as json

global hastaglist
hastaglist= []
def searchandsave(hastaglist):
    for i in range(len(hastaglist)):
        search_text='#'+hastaglist[i]
        # Open/Create a file to append data
        csvFile = open("data/"+search_text+'.csv', 'a')
        #Use csv Writer
        csvWriter = csv.writer(csvFile)
       
        for tweet in tweepy.Cursor(api.search,q=search_text,count=1000000,
                                   lang="en",
                                   since="2000-04-03").items(1000):
          # print (tweet.created_at, tweet.text)
           csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    

 


def initilizeTweppy():
    with open('TwitterApi_Keys.json') as f:
        data = json.load(f)
    #pprint(data)
    
    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']
    access_token = data['access_token']
    access_secret = data['access_secret']  
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    print(consumer_key)
    #Connect Api
    global api 
    api = tweepy.API(auth)

    #Error handling
    if (not api):
        print ("Problem connecting to API")  
def Saveextracthastags(search_text):
    
    
     # Open/Create a file to append datan
    csvFile = open("data/"+search_text+'.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
   
    for tweet in tweepy.Cursor(api.search,q=search_text,count=10000000,
                               lang="en",
                               since="2000-04-03").items(100000):
        #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
       for i in range(0, len(tweet.entities.get('hashtags'))):
           
           #print (tweet.entities.get('hashtags')[i]['text'])
           #print(len(tweet.entities.get('hashtags')))
           if((tweet.entities.get('hashtags')[i]['text'] in hastaglist)):
              # print("element is already in the list")
              pass
           else:
               hastaglist.append(tweet.entities.get('hashtags')[i]['text'])
             
        
               
                
       csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
       #hastaglist.append(tweet.entities.get('hashtags')[0]['text']);
       
    print(hastaglist)
def main():
  initilizeTweppy()
  Saveextracthastags("#BuildingAutomation")
  #searchandsave(hastaglist);
if __name__== "__main__":
  main()

