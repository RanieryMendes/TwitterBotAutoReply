import tweepy
import time
import dotenv
import os

dotenv.load_dotenv()

consumer_key= os.getenv('C_KEY')
consumer_secret= os.getenv('C_SECRET')

key= os.getenv('KEY_K')
secret= os.getenv('SECRET_S')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#api.update_status('palmeiras campeao do paulista...') 

meu_presidente = "Ah mas quer saber.. pipipopo pau no cu do Bolsonaro"

lulinha = "saudades lulinha <3 "


 # gets the text as well as the tweet position 

file_name = "last_seen.txt"


def read_last_tweet(file_name):
    file_read= open(file_name, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()

    return last_seen_id


def add_last_tweet(file_name, id_tweet):
    file_write = open(file_name, 'w')
    file_write.write(str(id_tweet))
    file_write.close()

    return





def reply():
    tweets = api.mentions_timeline(read_last_tweet(file_name), tweet_mode='extended') #i can pass the last id as an argument, it will provide only the new tweets
    for tweet in reversed(tweets):
        if "bolsonaro" in tweet.full_text.lower():
            print('Tweet about Bolsonaro found!')
            print(str(tweet.id) + ' ' + tweet.full_text)

            api.update_status("@" + tweet.user.screen_name + " " + meu_presidente + "... calm down it's just a bot test", tweet.id)
            try:
                 api.create_favorite(tweet.id)

            except tweepy.TweepError as e:

                print(e.reason)
            # for retweet use api.retweet(tweet.id) 
            add_last_tweet(file_name, tweet.id)
    tweets = api.mentions_timeline(read_last_tweet(file_name), tweet_mode='extended') #i can pass the last id as an argument, it will provide only the newtweets
    for tweet in reversed(tweets):
        if "lula" in tweet.full_text.lower():
            print('Tweet about Lula found!')
            print(str(tweet.id) + ' ' + tweet.full_text)

            api.update_status("@" + tweet.user.screen_name + " " + lulinha + "... calm down it's just a bot test", tweet.id)
            try:
               api.create_favorite(tweet.id)
           
            except tweepy.TweepError as e:
                print(e.reason)
           
            add_last_tweet(file_name, tweet.id)
                


while True:
    reply()
    time.sleep(45)


