from kafka import KafkaConsumer
import json


class Consumer:
    def __init__(self):
        pass

    def consume_events(self,topic):
        consumer = KafkaConsumer(topic,
                                # group_id='my-group',
                                value_deserializer=lambda m: json.loads(m.decode("utf-8")),
                                bootstrap_servers=['localhost:9092']
                                # consumer_timeout_ms=10000
                                 )
        return consumer

    # def save_to_mongo(self, topic_conciumer):
    #     events =self.consume_events(topic_conciumer)
    #     conect_to_mongo=mongo.Mongo()
    #     for message in events:
    #         doc = message.value
    #         conect_to_mongo.save(topic_conciumer,doc)
    #         # print(type(doc))
    #         # print(doc)
    #         retriever_text=conect_to_mongo.activate(topic_conciumer)
    #         if(message.offset % 100 == 0):
    #             print(message.offset)


    # def listen(self):
    #     for message in self.consumer:
    #         yield message.value

