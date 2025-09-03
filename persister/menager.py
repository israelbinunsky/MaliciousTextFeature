
from persister.consumer import Consumer
from persister.mongo import Mongo
import threading


class Menager:
    def __init__(self):
        self.tophc_enri_anti = "enriched_preprocessed_tweets_antisemitic"
        self.tophc_enri_not_anti = "enriched_preprocessed_tweets_not_antisemitic"

    def save_to_mongo(self, topic_conciumer):
        conc=Consumer()
        conect_to_mongo=Mongo()
        events = conc.consume_events(topic_conciumer)
        print("func")
        print(events)
        for message in events:
            doc = message.value
            print(doc)
            conect_to_mongo.save(topic_conciumer, doc)
            # print(type(doc))
            # retriever_text = conect_to_mongo.activate(topic_conciumer)
            if (message.offset % 100 == 0):
                print(message.offset)

def runner():
    menager = Menager()
    t1 = threading.Thread(target=menager.save_to_mongo, args=(menager.tophc_enri_anti,))
    t2 = threading.Thread(target=menager.save_to_mongo, args=(menager.tophc_enri_not_anti,))
    t1.start()
    t2.start()
runner()