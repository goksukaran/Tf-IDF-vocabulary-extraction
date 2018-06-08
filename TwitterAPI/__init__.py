import tweepy
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

# Get the User object for twitter...
user = api.get_user('twitter')
print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)