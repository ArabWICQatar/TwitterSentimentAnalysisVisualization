'''
scraps and stores tweets by airline
'''

import csv

sntTweets = csv.reader(open("search-data/sentimentUniqueTweets.csv", 'rb'))

def scrapTweets(airline):
    airwayTweet = csv.writer(open("search-data/"+airline+"Tweets.csv", "wb"))
    # store tweets by airways
    count = 1
    for row in sntTweets:
        r = row[2].lower()
        r = row[2].strip('#').strip('@')
        if airline in r:
            count = count + 1
            airwayTweet.writerow(row)
    print "# of rows", count

scrapTweets("qatarairways") # replace with emirates and etihadairways and run this script again
