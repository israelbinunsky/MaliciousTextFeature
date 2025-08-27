from pymongo import MongoClient

class Dal:
   def __init__(self, uri, dbname, collection):
       self.mongodb_client = MongoClient(uri)
       self.database = self.mongodb_client[dbname]
       self.collection = collection

   def get_collection(self,limit=100):
       collection = self.database[self.collection]
       collection = list(collection.find(filter=None, limit=limit))
       return collection

d = fetcher = Dal('mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/', 'IranMalDB', 'tweets')
d.get_collection()