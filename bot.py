import tweepy
import time

consumer_key='2BpD2cyGcMfOBD9SvC9Y108as'
consumer_secret='rfAkq8042vFYMz6jeMmMbJgW4zDp9egreRJvlgqmmPyOqfd2bC'
key='1257320699649114116-UAJjV3gfgdU0gUYWSbGGGx1RrLC0R4'
secret='g0Zuq2XJZ7BtT74uqvKcL3DKOPdmsJKVHMsNtayR4kUz1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME='last_seen.txt'
def readlastseen(FILE_NAME):
    read_file=open(FILE_NAME,'r')
    last_seen_id=int(read_file.read().strip())
    read_file.close()
    return last_seen_id

def store_lastseen(FILE_NAME,last_seen_id):
    write_file=open(FILE_NAME,'w')
    write_file.write(str(last_seen_id))
    write_file.close()
    return

def reply():
    tweets=api.mentions_timeline(readlastseen(FILE_NAME), tweet_mode='extended') #Returns the 20 most recent mentions, including retweets;extended keyword allows to cover mesgs of several para and linksS
    for tweet in reversed(tweets):
        if "#randomtweet" in tweet.full_text.lower():
            print("replied to id:"+str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Good luck //codepage", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_lastseen(FILE_NAME,tweet.id)
while(True):
    reply()
    time.sleep(15) # bot replies to the tweet in 15 sec
