import os
from kafka import KafkaProducer,KafkaConsumer
import json


class Subskriber:
    def __init__(self):
        self.topic_anti = "raw_tweets_antisemitic"
        self.topic_no_anti = "raw_tweets_not_antisemitic"


    def get_consumer_events(self,topic):
        consumer = KafkaConsumer(topic,
                                # group_id='my-group',
                                value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                bootstrap_servers=['localhost:9092']
                                # consumer_timeout_ms=10000
                                 )
        return consumer


    def consumer_messages(self,topic):
        events = self.get_consumer_events(topic)
        final_data = []
        for message in events:
            print(f"yes, {message}")
            a = cleaner.clean(message.value)
            publisher.publish_message(a)
        events.close()



a=Subskriber()
# a.consumer_messages("raw_tweets_not_antisemitic")
b=a.get_consumer_events("raw_tweets_not_antisemitic")
s=a.consumer_messages(a.topic_anti)
e=a.consumer_messages(a.topic_no_anti)
print(s,e)