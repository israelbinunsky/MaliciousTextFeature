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
       return collection



async def main():
    d = Dal()
    skip = 0
    limit = 100
    while True:
        docs = await d.get_collection(skip, limit)
        for doc in docs:
            print(doc)
        skip += limit
        await asyncio.sleep(8)

asyncio.run(main())
