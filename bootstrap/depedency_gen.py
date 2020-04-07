import json
service={
  "Communication_Module":
   {
     "ip": "localhost",
     "port" : "6010"
     
   },
   "Server_LifeCycle":
   {
     "ip": "localhost",
     "port" : "9090"
   },
   "Service_LifeCycle" :
   {
     "ip": "localhost",
     "port" : "9090"
   },
   "Schedular" :
   {
     "ip": "localhost",
     "port" : "9090"
   },
   "dependency" : ['Communication_Module','Server_LifeCycle','Service_LifeCycle','Schedular']
}
with open('dependency.json', 'w') as json_file:
  json.dump(service, json_file)