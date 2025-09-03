from kafka import KafkaProducer,KafkaConsumer
import json

class Publisher:
    def __init__(self):
        self.producer = None
        self.get_producer_config()


    def get_producer_config(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x:
                                 json.dumps(x,default=str).encode('utf-8'))
        print(self.producer.config)
        return self.producer

    def publish_message(self,topic,message: dict):
        self.producer.send(topic,message)

a=Publisher()



