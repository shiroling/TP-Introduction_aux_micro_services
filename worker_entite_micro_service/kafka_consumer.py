from kafka import KafkaConsumer
from json import loads

kafka_host_port = 'broker:9092' 
topic= "mon_topic"

def create_consumer(topic_id): 
	consumer = KafkaConsumer (
		topic,
		bootstrap_servers=[kafka_host_port],
		auto_offset_reset='earliest',
		enable_auto_commit=True,
		consumer_timeout_ms=1000,
		group_id='group',
		value_deserializer=lambda x: loads(x.decode('utf-8')))
	return consumer

def read_from_topic (consumer):
	data = []
	for message in consumer:
		data.append(message.value)
	return data