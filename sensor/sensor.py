import json
from bson import json_util

def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')

def sensor_run(id,typ,loc,range,ip,port):
	
	with open('meta.json') as f:
  		meta = json.load(f)

  	rang=meta[typ]['range']
  	frequency=meta[typ]['frequency']
  	type_=meta[typ]['type']
  	if type_ == 'real':
	  	min_limit_of_data=meta[typ]['min']
	  	max_limit_of_data=meta[typ]['max']


  	topic= typ

  	message={}
  	message['type']=typ
  	message['id']= id
  	message['location']=loc
  	message['location_type']=None #GPS or room no
  	message['range']=rang
  	message['data']=random.randrange(20, 40)

  	from kafka import KafkaProducer
	producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
	producer.send(topic,json.dumps(message, default=json_util.default).encode('utf-8'))

def sensor(id,typ,loc,range,ip,port,start_time=None,end_time=None,itr=None):
	if itr is None:
		while 1:
			sensor_run(id,typ,loc,range,ip,port)
	else:
		for i in range (itr):
			sensor_run(id,typ,loc,range,ip,port)




