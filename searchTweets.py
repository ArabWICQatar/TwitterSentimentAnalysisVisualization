'''
To authenticate and connect with Twitter
Use search REST API to gather tweets from a list of keywords
Store tweets as a csv file
'''

import tweepy
import sys
import csv

# to force utf-8 encoding on entire program
reload(sys)
sys.setdefaultencoding('utf8')

alltweets = csv.writer(open("search-data/searchTweets.csv", 'ab'))

def search(keywords):
    access_key = "your app access key here"
    access_secret = "your app access token here"
    consumer_key = "your app consumer key here"
    consumer_secret = "your app consumer secret here"

    #to authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    count = 1;
    for tweet in api.search(keywords,'en', count = 100):
        created_at =  tweet.created_at  # accessing tweet time
        tweet_id = tweet.id_str         # accessing tweet id
        tweet_text = tweet.text         # accessing tweet text
        print "gathered tweet ",count
        count = count + 1
        alltweets.writerow([created_at, tweet_id, tweet_text])

#search("Qatar Airways") # to search one keyword at a time

file = open('hashtags-keywords.txt', 'r') # contains a list of keywords
queries = file.readlines()

for q in queries:
    # read one keyword at a time
    print "----"
    print q
    search(q)
