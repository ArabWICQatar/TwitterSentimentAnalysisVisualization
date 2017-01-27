'''
compute total, positive, negative and neutral tweets for each airline
'''

import csv

def getStats(s, fileRead):
    tot = 0;
    pos = 0;
    neg = 0;
    neu = 0;
    for row in fileRead:
        tot = tot + 1;
        if row[4] == "positive":
            pos = pos + 1;
        elif row[4] == "negative":
            neg = neg + 1;
        elif row[4] == "neutral":
            neu = neu + 1;
    print "Tweets Stats for", s
    print "total tweets: ", tot
    print "positive: ", pos
    print "negative: ", neg
    print "neutral: ", neu
    results.writerow([s, tot, pos, neg, neu])

qatarTweets = csv.reader(open("search-data/qatarairwaysTweets.csv", "rb"))
emirateTweets = csv.reader(open("search-data/emiratesTweets.csv", "rb"))
etihadTweets = csv.reader(open("search-data/etihadairwaysTweets.csv", "rb"))
results = csv.writer(open("search-data/results.csv", "wb"))

getStats("qatar", qatarTweets)
getStats("emirates", emirateTweets)
getStats("etihad", etihadTweets)
