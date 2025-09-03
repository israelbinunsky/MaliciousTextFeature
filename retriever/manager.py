
from retriever.dal import Dal
from retriever.publisher import Publisher

dl=Dal()
pub=Publisher()

def manager():
    producer =None
    try:
        producer = pub.get_producer_config()
        for data in dl.get_100_doc_every_60_sec(limit=100):
            splited_data=dl.get_splited_data(data)
            for text_anti in splited_data["antisemitic"]:
                pub.publish_message(pub.topic_anti,text_anti)
            for text_not_anti in splited_data["non_antisemitic"]  :
                pub.publish_message(pub.topic_no_anti,text_not_anti)
            # print(f"Sent {len(splited_data['antisemitic'])} antisemitic, "
            #       f"{len(splited_data['non_antisemitic'])} non_antisemitic")
            # print("pushed to kafka")

    except Exception as e:
        print(f"error: {e}")
    finally:
        if producer:
            producer.flush()

manager()





