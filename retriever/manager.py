from dal import Dal
from publisher import Publisher
dl=Dal()
pub=Publisher()

def maneger():
    dl.get_collection()
    producer =pub.get_producer_config()
    pub.publish_message(producer,pub.topic1,)

    print('!!!')





