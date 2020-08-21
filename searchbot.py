import tweepy
import time

consumer_key='2BpD2cyGcMfOBD9SvC9Y108as'
consumer_secret='rfAkq8042vFYMz6jeMmMbJgW4zDp9egreRJvlgqmmPyOqfd2bC'
key='1257320699649114116-UAJjV3gfgdU0gUYWSbGGGx1RrLC0R4'
secret='g0Zuq2XJZ7BtT74uqvKcL3DKOPdmsJKVHMsNtayR4kUz1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag= "100daysofcode" #for retweeting tweets with only specific hashtags; for 2 hashtags use tuple i.e ("100daysofcode","python")
tweetNumber= 10

tweets= tweepy.Cursor(api.search,hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("retweet done!!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchBot()
