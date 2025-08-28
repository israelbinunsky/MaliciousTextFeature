import os
MONGO_USER = os.getenv("MONGO_USER", "IRGC_NEW")
MONGO_PASS = os.getenv("MONGO_PASS", "iran135")
MONGO_DB = os.getenv("MONGO_DB", "IranMalDB")
MONGO_URI = os.getenv('MONGO_URI', f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.6ycjkak.mongodb.net/' )
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "tweets")

