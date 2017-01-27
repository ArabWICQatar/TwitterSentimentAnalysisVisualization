'''
uses TextBlob to obtain sentiment for unique tweets
'''

import csv
from textblob import TextBlob
import sys

# to force utf-8 encoding on entire program
reload(sys)
sys.setdefaultencoding('utf8')

alltweets = csv.reader(open("search-data/uniqueSearchTweets.csv", 'rb'))
sntTweets = csv.writer(open("search-data/sentimentUniqueTweets.csv", "wb"))

for row in alltweets:
    blob = TextBlob(row[2])
    print blob.sentiment.polarity
    if blob.sentiment.polarity > 0:
        sntTweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "positive"])
    elif blob.sentiment.polarity < 0:
        sntTweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "negative"])
    elif blob.sentiment.polarity == 0.0:
        sntTweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "neutral"])
