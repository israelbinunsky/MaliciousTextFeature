# from Preprocessor.subscriber import Subscriber
# from retriever.publisher import Publisher
from kafka import KafkaProducer,KafkaConsumer
import json
from publisher_therd import Publisher
from enricher import Enricher
import threading

class Subscriber2:
    def __init__(self):
        self.topic_pro_anti="preprocessed_tweets_antisemitic"
        self.topic_pro_not_anti="preprocessed_tweets_not_antisemitic"
        self.tophc_enri_anti="enriched_preprocessed_tweets_antisemitic"
        self.tophc_enri_not_anti="enriched_preprocessed_tweets_not_antisemitic"


        # def subscribe_2(self,topic_conciumer):
    #     Subscriber.get_consumer_events(topic_conciumer)
    def get_consumer_events(self,topic):
        consumer = KafkaConsumer(topic,
                                # group_id='my-group',
                                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                bootstrap_servers=['localhost:9092']
                                # consumer_timeout_ms=10000
                                 )
        return consumer

    def consumer_messages(self, topic_conciumer, topic_producer ):
        events =self.get_consumer_events(topic_conciumer)
        pub =Publisher()
        enri=Enricher()
        for message in events:

            doc = message.value
            # print(type(doc))
            # print(doc)
            retriever_text=enri.activate_enricher(doc)
            if(message.offset % 100 == 0):
                print(message.offset)
            pub.publish_message(topic_producer,retriever_text)



a=Subscriber2()
t1=threading.Thread(target=a.consumer_messages, args=(a.topic_pro_anti, a.tophc_enri_anti))
t2 =threading.Thread(target=a.consumer_messages, args=(a.topic_pro_not_anti, a.tophc_enri_not_anti))
t1.start()
t2.start()