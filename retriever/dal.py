from pymongo import MongoClient
import config
import time

class Dal:
   def __init__(self):
       self.USER = config.MONGO_USER
       self.PASS = config.MONGO_PASS
       self.uri = config.MONGO_URI

       self.mongodb_client = MongoClient(self.uri)
       self.database = self.mongodb_client[config.MONGO_DB]
       self.collection = config.MONGO_COLLECTION

   def get_collection(self, skip=0 ,limit=100):
       collection = self.database[self.collection]
       collection = list(collection.find().sort( 'CreateDate', 1).skip(skip).limit(limit))
       # print("you gat a collection")
       return collection

   def get_splited_data(self, collection):
       result = {
           "antisemitic": [],
           "non_antisemitic": []
       }
       for doc in collection:
           # doc_id = str(doc.get("_id"))
           if doc["Antisemitic"] == 1:
               result["antisemitic"].append(doc)

           else:
               result["non_antisemitic"].append(doc)
       # print(result["antisemitic"][0],result["non_antisemitic"][0])
       return result


   def get_100_doc_every_60_sec(self, limit = 100):
       # d = Dal()
       skip = 0
       while True:
           docs =  self.get_collection(skip, limit)
           for doc in docs:
               print(doc)
           yield docs
           skip += limit
           time.sleep(60)



a=Dal()
b=a.get_collection()
a.get_splited_data(b)




