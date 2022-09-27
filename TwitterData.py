from asyncio.windows_events import NULL
import configparser
import tweepy
import re
import pandas as pd 

class TwitterData : 

    monitored_tickers = []
    twitter_auth_keys = NULL
    auth = NULL
    config = configparser.ConfigParser()
    tweets = NULL
    urls = []

    def __init__(self, monitored_tickers):
        self.monitored_tickers = monitored_tickers
        self.config.read('config.ini')
        self.twitter_auth_keys = {
            "consumer_key"        : self.config['twitter']['consumer_key'],
            "consumer_secret"     : self.config['twitter']['consumer_secret'],
            "access_token"        : self.config['twitter']['access_token'],
            "access_token_secret" : self.config['twitter']['access_token_secret'],
            "bearer"              : self.config['twitter']['bearer']
        }
        self.auth = tweepy.OAuthHandler(
                self.twitter_auth_keys['consumer_key'],
                self.twitter_auth_keys['consumer_secret']
        )
        self.auth.set_access_token (
                self.twitter_auth_keys['access_token'],
                self.twitter_auth_keys['access_token_secret']
        )        

    #Clean the tweets : 
    def cleanTweet(self, twt):
        for ticker in self.monitored_tickers:
            twt = re.sub(f'#{ticker}', ticker, twt)
        twt = re.sub('#[A-Za-z0-9]+', '', twt)
        twt = re.sub('@[A-Za-z0-9]+', '', twt)
        twt = re.sub('\\n', '', twt)
        twt = re.sub('https:\/\/\S+', '', twt)
        return twt

    def getTweets(self, hashtag):
        api = tweepy.API(self.auth, wait_on_rate_limit=True)
        #term to search for
        search_term = f"#{hashtag} until:2022-08-18 -filter:retweets"
        #count : number of results per page
        tweets = tweepy.Cursor(api.search_tweets, search_term, count=1000, lang='en').items(1000)
        return [self.cleanTweet(tweet.text) for tweet in tweets]

    def getData(self):
        self.tweets = {ticker:self.getTweets(ticker) for ticker in self.monitored_tickers}
        for ticker in self.monitored_tickers:
            df = pd.DataFrame(self.tweets[ticker], columns=['Text'])
            self.tweets[ticker] = df.drop_duplicates()['Text'].to_numpy().tolist()
            
        #df['urls'] = 'Twitter'
        return self.tweets


