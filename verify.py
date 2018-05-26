import config 

from datetime import datetime
from operator import attrgetter
import tweepy

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def is_target_tweet_real(screen_name, target_tweet_status, target_tweet_time):
    """Returns whether or not a given tweet exists in the user's timeline. 

    TODO: Add functionality to measure similarity of target tweet to a given tweet.

    Keyword arguments:
    screen_name -- the screen name of the user who created the tweet
    target_tweet_status -- the status of the tweet
    target_tweet_time -- the time at which the tweet was created
    """

    tweets = api.user_timeline(screen_name = screen_name, count = 200)
    for tweet in tweets: 
        if target_tweet_status in tweet.text:
            print('Verified: Tweet exists.')
            return True
    
    oldest_tweet = min(tweets, key=attrgetter('created_at')) 
    if oldest_tweet.created_at > target_tweet_time: 
        print('Verified: Tweet does not exist.')
        return False
    
    #TODO: Add functionality to repeat until the target tweet's time has been covered. 
    print('Unable to verify: Range of tweets collected does not include time when target Tweet was created.')
