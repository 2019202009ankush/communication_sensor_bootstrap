import producer
import threading
import time
import producer_json


import json
from bson import json_util

def ApplicationManager_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='ApplicationManager_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name)
			th.start()

def ApplicationManager_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('ApplicationManager_to_ServiceLifeCycle',mess)



def ServiceLifeCycle_to_DeployManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='ServiceLifeCycle_to_DeployManager'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name)
			th.start()

def DeploymentManager_to_SensorManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='DeploymentManager_to_SensorManager'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name)
			th.start()
		
def ApplicationManager_to_Scheduler_interface(func_name):
	from kafka import KafkaConsumer
	topic='ApplicationManager_to_Scheduler'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name)
			th.start()


def DeploymentManager_to_RuntimeServer_interface(func_name):
	from kafka import KafkaConsumer
	topic='DeploymentManager_to_RuntimeServer'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name)
			th.start()

		
def RuntimeServer_to_ActionServer_interface(func_name):
	from kafka import KafkaConsumer
	topic='RuntimeServer_to_ActionServer'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name)
			th.start()

def Sersor_Stream(typ):
	from kafka import KafkaConsumer
	topic=typ
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			yield mess
	return (get_stream())


# import os
# os.system('docker run --rm -it -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 -e ADV_HOST=127.0.0.1 landoop/fast-data-dev')
# import json	
# with open('topic.json') as f:
# 		meta = json.load(f)
# l=meta['topic']
# for topic in l:
# 	print('Creating topic ', topic)
# 	producer.send_message(topic,"start")