Team5 group 3 (2019202009)(Explined in video link: https://www.youtube.com/watch?v=rixFLCBNLao&t=333s)(Note that due to processing video is lagging behind sound comes first please bear with it)
 

Bootstrap:
	6 part
		init.py
		start.sh
		docker-compose.yml
		config.json
		report.json
		requirement.txt
	Description:user will come and give the config.json where ip,port, ip pool and denpendenncy is given init.py will read that
	json file and try to on the plafrom according to dependency(priority). There will be some standard set up like install requirement.txt
	making  a docker container (docker-compose up) accroding to docker-compose.yml (standerd  system dependency) which will be handeled by
	start.sh.
 	
	init.py will combine both the thing (uping the platfrom based on config.json and run start.sh ) and at the end it will generate a report.json 
	which indicate which module is running on which ip port.
  
Communication Module:
	6 part:
		producer interface
		consumer interface
		stram 
		Dummy Application Manager
		Dummy ServiceLifeCycle
		topic.json
	Description:
	platfrom has all list of topic that is mentioned in topic.json.Communication module will read the json and create the topic(not required in python-kafka; so i comment
	that code; in pyKafka it is required). Now communication module has 3 type of interface- producer interface,consumer interface,stream interface. Using producer interfaces
	any module can send data to another module via kafka.This module take the data from the porducer module and dumps the data to Kafka topic named as "ProducerName_to_ConsumerName".
	This interface is named as "ProducerName_to_ConsumerName_Producer_interface". Using consumer interfaces a consumer module can listen to topic  "ProducerName_to_ConsumerName" in
	passive mode and wait some event to run based on json data on the topic  "ProducerName_to_ConsumerName" . When some data comes communication_module fir up a thread and call the function
	(event) that is given when the consumer interface is called (interface argument). Stream interface is for data streaming purpose . It is not event driven(not fire any thread) but yeild the 
	data and return for real time stream.
	For demo dummy application manager and dummy ServiceLifeCycle is made. Here Application Manager is producer and ServerviceLifeCycle is consumer and ServerviceLifeCycle want to run a function call event1 
	based on data that comes from Application Manager. Application Manager will call the producer interface to dumps some json data on topic "ApplicationManager_to_ServerviceLifeCycle".
	ServerviceLifeCycle will call the consumer interface by passing function name as argument and wait for data to run some event based on the data. When data comes communication module will fire up a thread 
	and run that function on that thread.

	Note: all the module that want to communicate with each other should import communication_module.
Sensor:
	4 part:
		Sensor Simulator
		meta.json
		dummy Sensor manager
		dummy Algorithm
	Description: If any one want to run the sensor simulator , it has to give a meta.json file which will contain information about sensor type,range,location, location type,minmun value of data,maximum value of data.
	After that it has to call sensor method in sensor.py . Based on the argument the sensor method will call sensor_run  method . Based on argument sensor_run will read the meta file to crate a json message and finally it 
	dumps the json on kafka topic. Now any module can fetch the stram using communication_module stream interface.
	Note: the use of meta enable a user to tell the simuator about the configuration of the sensor . Ex- user can mention that temparture sensor min_data should be 20 and max_data shold be 40 and sensor radius shoud be 20 meter.
	For demo I have created a dummy Sensor Manager which want to simulate temperautre sensor and dummy Algorithm which want to fetch the sensor stream .