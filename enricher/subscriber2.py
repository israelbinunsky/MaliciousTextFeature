from Preprocessor.subscriber import Subscriber
from retriever.publisher import Publisher
class Subscriber2:
    def __init__(self):
        self.topic_pro_anti="preprocessed_tweets_antisemitic"
        self.topic_pro_not_anti="preprocessed_tweets_not_antisemitic"


    # def subscribe_2(self,topic_conciumer):
    #     Subscriber.get_consumer_events(topic_conciumer)

    def consumer_messages(self, topic_conciumer, topic_producer, ):
        events = Subscriber.get_consumer_events(topic_conciumer)
        pub = Publisher()
        for message in events:
            retriver_text=pro.new_param(message.value)
            pub.publish_message(topic_producer,retriver_text)

