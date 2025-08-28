from pymongo import MongoClient
from datetime import datetime
import config
from consumer import Consumer

class Mongo:
    def __init__(self, uri=config.MONGO_URI, db_name=config.MONGO_DB):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collections = {
            "antisemitic": self.db["tweets_antisemitic"],
            "not_antisemitic": self.db["tweets_not_antisemitic"]
        }

    def save(self, topic, message):
        doc = {
            "createdate": datetime.utcnow(),
            "antisemietic": message.get("antisemietic", 0),
            "original_text": message.get("original_text", ""),
            "clean_text": message.get("clean_text", ""),
            "sentiment": message.get("sentiment", ""),
            "weapons_detected": message.get("weapons_detected", []),
            "relevant_timestamp": message.get("relevant_timestamp", "")
        }
        if topic in self.collections:
            self.collections[topic].insert_one(doc)

    def activate(self, topic):
        con = Consumer(topic)
        message = con.listen()
        self.save(topic, message)
