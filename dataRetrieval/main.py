from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
MONGO_URI = "mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/"
DB_NAME = "IranMalDB"

# יצירת לקוח MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

app = FastAPI()



@app.get("/anticemititic")
async def get_data_anticemititic():
    def get_collection1_data():
        collection1 = db["tweets_antisemitic"]
        data = list(collection1.find({}))
        return data
@app.get("/not_anticemititic")
async def get_data_not_anticemititic():
    def get_collection1_data():
        collection1 = db["tweets_not_antisemitic"]
        data = list(collection1.find({}))
        return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)