from kafka import KafkaConsumer
import json


class Consumer:
    def __init__(self, topic, bootstrap_servers="localhost:9092"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

    def listen(self):
        for message in self.consumer:
            yield message.value
