## TwitterSentimentAnalysisVisualization
A simple Sentiment analysis and visualization for analyzing the sentiment of three popular Airlines in Middle East: Qatar Airways, Emirates and Etihad. This project is for the 101 workshops by ArabWICQatar.

Dependencies:

Python 2.7

Python modules: 

Tweepy :- '''python pip install -U tweepy '''
Pandas :- '''python pip install -U pandas '''
NLTK :- '''python pip install -U nltk '''
TextBlob :- '''python pip install -U textblob  '''

### Steps to run:
1. DATA COLLECTION

⋅⋅* Create a Twitter app and enter the app credentials in searchTweets.py file

⋅⋅* Create new folder, search-data and run the searchTweets.py script. searchTweets.csv file containing gathered tweets will be stored inside search-data folder


2. PREPROCESSING - Data Cleaning

⋅⋅* Run remDupTweets.py script to remove duplicate tweets from the searchTweets.csv and unique tweets will be stored in uniqueSearchTweets.csv inside search-data folder


3. SENTIMENT ANALYSIS using TextBlob

⋅⋅* Run sentiment.py script to obtain sentiment for tweets. All unique tweets with sentiment results will be stored in sentimentUniqueTweets.csv inside search-data folder


4. VISUALIZATION using Highcharts

⋅⋅* To prepare the data for visualization, tweets for each airline are scrapped from the sentimentUniqueTweets.csv and stored. Run the scrapAirlineTweets.py to obtain tweets by airline in the search-data folder in form of csvs.

⋅⋅* The total positive, negative and neutral sentiment for each airline is computed in the computeResults.py . The results.csv stored in search-data folder has the number of totalTweets, positive tweets, negative tweets and neutral tweets by airline.

⋅⋅* The files inside lib folder containing jquery and highcharts.js files are used to generate visualizations. Dobuleclik or open the results.html file in a browser to view the visualization for obtained sentiment results.

