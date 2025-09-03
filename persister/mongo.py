from pymongo import MongoClient
from datetime import datetime
import config
from consumer import Consumer

class Mongo:
    def __init__(self, uri="mongodb://localhost:27017",db_name="local_iran_tweets"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collections = {
            "enriched_preprocessed_tweets_antisemitic": self.db["tweets_antisemitic"],
            "enriched_preprocessed_tweets_not_antisemitic": self.db["tweets_not_antisemitic"]
        }
        self.tweets_antisemitic="tweets_antisemitic"
        self.tweets_not_antisemitic="tweets_not_antisemitic"

        print(self.client)

    def save(self, topic, message):
        print(">>> save called with:", topic, message)
        doc = {
            "createdate": datetime.now(),
            "antisemietic": message.get("antisemietic", 0),
            "original_text": message.get("original_text", ""),
            "clean_text": message.get("clean_text", ""),
            "sentiment": message.get("sentiment", ""),
            "weapons_detected": message.get("weapons_detected", []),
            "relevant_timestamp": message.get("relevant_timestamp", "")
        }

        res = self.collections[topic].insert_one(doc)
        print(res)
    # def activate(self, topic):
    #     con = Consumer()
    #     for message in con():
    #         self.save(topic, message)
