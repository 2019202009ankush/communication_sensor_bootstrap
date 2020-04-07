import producer
import threading
import time

def start(ip,port):
	ip= 'localhost'
	port = 9092
	
	with open('topic_meta.json') as f:
  		meta = json.load(f)
  	l=meta['topic']['topic']
  	for topic in l:
  		producer.send_message(topic,"start")

def ApplicationManager_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='ApplicationManager_to_ServiceLifeCycle'
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		data=json.loads(mess.decode('utf-8'))
		th = threading.Thread(target=func_name, args=(data))
 		th.start()

def ServiceLifeCycle_to_DeployManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='ServiceLifeCycle_to_DeployManager'
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		data=json.loads(mess.decode('utf-8'))
		th = threading.Thread(target=func_name, args=(data))
 		th.start()
		

def DeploymentManager_to_SensorManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='DeploymentManager_to_SensorManager'
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		data=json.loads(mess.decode('utf-8'))
		th = threading.Thread(target=func_name, args=(data))
 		th.start()
 		
def ApplicationManager_to_Scheduler_interface(func_name):
	from kafka import KafkaConsumer
	topic='ApplicationManager_to_Scheduler'
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		data=json.loads(mess.decode('utf-8'))
		th = threading.Thread(target=func_name, args=(data))
 		th.start()


def DeploymentManager_to_RuntimeServer_interface(func_name):
	from kafka import KafkaConsumer
	topic='DeploymentManager_to_RuntimeServer'
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		data=json.loads(mess.decode('utf-8'))
		th = threading.Thread(target=func_name, args=(data))
 		th.start()
 		
def RuntimeServer_to_ActionServer_interface(func_name):
	from kafka import KafkaConsumer
	topic='RuntimeServer_to_ActionServer'
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		data=json.loads(mess.decode('utf-8'))
		th = threading.Thread(target=func_name, args=(data))
 		th.start()

def Sersor_Stream(type):
	from kafka import KafkaConsumer
	topic='RuntimeServer_to_ActionServer'
	consumer = KafkaConsumer(topic)
	def get_stream():
		for mess in consumer:
			data=json.loads(mess.decode('utf-8'))
			yield data
	return (get_stream())


    
	