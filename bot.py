import tweepy

consumer_key= "0fPjw1XW3bkJJYfgb1aMTVdOp"
consumer_secret= "UvqWrB46HfLGLHpdPcuW92oKIsioYkybKgbTgat28bRn6L20pQ"

key= "198663868-PaojlwJrAs2oHAei3EA22GWLx5aVkCM0MZ7xTxzs"
secret= "0lTayeWDgzS2GzSWgRdIXTR5j84ufLx8knFuOyFNUwbQO"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#api.update_status('palmeiras campeao do paulista...') 


tweets = api.mentions_timeline()
print(tweets[1].text) # gets the text as well as the tweet position 