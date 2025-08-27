from kafka import KafkaProducer,KafkaConsumer
import json

class Publisher:
    def __init__(self):
        # self.event1={"App":"Producer 1"}
        # self.event2={"App": "Producer 2"}
        self.topic_anti= "raw_tweets_antisemitic"
        self.topic_no_anti= "raw_tweets_not_antisemitic"


    def get_producer_config(self):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x:
                                 json.dumps(x,default=str).encode('utf-8'))
        print(producer.config)
        return producer

    def publish_message(self,producer,topic,message):
        producer.send(topic, message)


a=Publisher()


        #Publish message to a topic
        # publish_message(get_producer_config(),"topic1",event)