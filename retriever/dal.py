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

       return result


   def main(self):
       d = Dal()
       skip = 0
       limit = 100
       while True:
           docs = d.get_collection(skip, limit)
           for doc in docs:
               print(doc)
           skip += limit
           time.sleep(5)



# a=Dal()
# a.main()


