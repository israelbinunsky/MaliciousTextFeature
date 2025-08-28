from winreg import error

from dal import Dal
from publisher import Publisher
import time
dl=Dal()
pub=Publisher()

def manager():
    producer =None
    try:

        producer = pub.get_producer_config()
        while True:
            data=dl.get_collection()
            s=dl.get_splited_data(data)
            pub.publish_message(producer, pub.topic_anti,s["antisemitic"])
            pub.publish_message(producer, pub.topic_no_anti,s["non_antisemitic"])
            print("pushed to kafka")
            time.sleep(5)
    except Exception as e:
        print(f"error: {e}")
    finally:
        if producer:
            producer.flush()


manager()





