import tweepy
import time
import jupyter

auth = tweepy.OAuthHandler('IsMYLNn6ROLwlThlN7dxrPmEX', 'dESLFVEzkS5RnTHCx6Jj6jtBSAGvjQ4QfxPsndBW9DJomluK25')
auth.set_access_token('808852656-g0TAJJOjyXA1mgIbUaLxujitC2ee7KzEigDa7qaV', 'aNJiGTPvAY4LZCgMzH9EFbssYqnnfIfKG3Gd48ks26pGU')

api = tweepy.API(auth)
user= api.me()

# generous Bot

def limit_handle(cursor):
    try:
        while(True):
            yield cursor.next()
    except tweepy.RateLimitError as err:
        time.sleep(1000)


#for follower in tweepy.Cursor(api.followers).items():
#       follower.follow()
search_string= 'Mohammed'
numberOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break



