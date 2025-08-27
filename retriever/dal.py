from pymongo import MongoClient
import config
import asyncio

class Dal:
   def __init__(self):
       self.USER = config.MONGO_USER
       self.PASS = config.MONGO_PASS
       self.uri = config.MONGO_URI
       self.mongodb_client = MongoClient(self.uri)
       self.database = self.mongodb_client[config.MONGO_DB]
       self.collection = config.MONGO_COLLECTION

   async def get_collection(self, skip=0 ,limit=100):
       collection = self.database[self.collection]
       collection = list(collection.find().sort( 'CreateDate', 1).skip(skip).limit(limit))
       for doc in collection:
           print(doc)
       return collection

async def main():
    dal = Dal()
    skip = 0
    limit = 100
    while True:
        await dal.get_collection(skip, limit)
        skip += limit
        await asyncio.sleep(5)

asyncio.run(main())
