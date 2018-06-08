import tweepy
import csv
import pandas as pd
from tweepy import OAuthHandler


try:
    import json
except ImportError:
    import simplejson as json
consumer_key = 'T4S8NM1zImZaJrdh2eoojzEsK'
consumer_secret = 'vLVD9nPSnLoxAgQonJZC7Mrp0GLliQFxcXg0d6nMP1b6DgXwum'
access_token = '1004965282429980672-m3bviyqV4DigZz1mxubm8iH46sbpDn'
access_secret = 'ZH41wTFQuYKYhP2oF8vIsbTz2AUpnD8ByaOBQ1E9bt2Um'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

search_text = "#Building Automation"
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
search_number = 10
for tweet in tweepy.Cursor(api.search,q=search_text,count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])