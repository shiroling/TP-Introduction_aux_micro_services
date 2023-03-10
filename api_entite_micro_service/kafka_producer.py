from kafka import KafkaProducer 
from json import dumps

kafka_host_port = 'broker:9092'
topic = 'mon_topic'

def put_in_topic(data): 
    try:
        producer = KafkaProducer (bootstrap_servers=[kafka_host_port],
                                    value_serializer=lambda x:
                                    dumps (x).encode('utf-8'))
        producer.send(topic, value=data)
        return True
    except:
        return False