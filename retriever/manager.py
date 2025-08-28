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
            splited_data=dl.get_splited_data(data)
            for text_anti in splited_data["antisemitic"]:
                pub.publish_message(pub.topic_anti,text_anti)
            for text_not_anti in splited_data["non_antisemitic"]  :
                pub.publish_message(pub.topic_no_anti,text_not_anti)
            print("pushed to kafka")
            time.sleep(5)
    except Exception as e:
        print(f"error: {e}")
    finally:
        if producer:
            producer.flush()


manager()





