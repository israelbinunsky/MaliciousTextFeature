import os
from kafka import KafkaProducer,KafkaConsumer
import json
from processor import Processor
from retriever.publisher import Publisher
import threading

class Subscriber:
    def __init__(self):
        self.topic_anti = "raw_tweets_antisemitic"
        self.topic_no_anti = "raw_tweets_not_antisemitic"
        self.topic_pro_anti="preprocessed_tweets_antisemitic"
        self.topic_pro_not_anti="preprocessed_tweets_not_antisemitic"




    def get_consumer_events(self,topic):
        consumer = KafkaConsumer(topic,
                                # group_id='my-group',
                                value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                bootstrap_servers=['localhost:9092']
                                # consumer_timeout_ms=10000
                                 )
        return consumer


    def consumer_messages(self,topic_sub,topic_pub):
        events = self.get_consumer_events(topic_sub)
        pro=Processor()
        pub = Publisher()
        for message in events:
            clean_text=pro.new_param(message.value)
            pub.publish_message(topic_pub,clean_text)





a=Subscriber()
t1=threading.Thread(target=a.consumer_messages, args=(a.topic_anti, a.topic_pro_anti))
t2 =threading.Thread(target=a.consumer_messages, args=(a.topic_no_anti, a.topic_pro_not_anti))
t1.start()
t2.start()
# # a.consumer_messages("raw_tweets_not_antisemitic")
# # b=a.get_consumer_events("raw_tweets_not_antisemitic")
# s=a.consumer_messages(a.topic_anti,a.topic_pro_anti)
# e=a.consumer_messages(a.topic_no_anti,a.topic_pro_not_anti)
# print(s,e)