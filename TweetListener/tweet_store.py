from pymongo import MongoClient


def store(tweet):
    client = MongoClient('localhost', 27017)
    db = client.twitterdb
    col = db.tweets

    return col.insert_one(tweet).inserted_id
