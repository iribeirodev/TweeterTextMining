import yaml
from tweepy import OAuthHandler
from tweepy import Stream
from TweetListener import tweet_listener

# Get application config keys from yml file
def setup_keys():
    cfg = {}
    with open("config.yml", "r") as yml_file:
        cfg = yaml.load(yml_file)
    return cfg


app_config = setup_keys()

auth = OAuthHandler(app_config["consumer_key"], app_config["consumer_secret"])
auth.set_access_token(app_config["access_token"], app_config["access_token_secret"])

myListener = tweet_listener.ThisListener()
myStream = Stream(auth, listener=myListener)

myStream.filter(track=app_config["key_words"])
myStream.disconnect()

