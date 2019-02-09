from tweepy.streaming import StreamListener
from TweetListener import tweet_store
import json


# Classe para armazenar no MongoDB os streams do Twitter
class ThisListener(StreamListener):
    def on_data(self, this_data):
        tweet = json.loads(this_data)

        this_tweet = {
            "created_at": tweet["created_at"],
            "id_str": tweet["id_str"],
            "text": tweet["text"],
        }

        tweet_store.store(this_tweet)
        print(this_tweet)

        return True