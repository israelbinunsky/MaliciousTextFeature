from dal import Dal
from publisher import Publisher
dl=Dal()
pub=Publisher()

def manager():
    data=dl.get_collection()
    s=dl.get_splited_data(data)
    producer=pub.get_producer_config()
    pub.publish_message(producer, pub.topic_anti,s["antisemitic"])
    pub.publish_message(producer, pub.topic_no_anti,s["non_antisemitic"])
    print("pushed to kafka")







