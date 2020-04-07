with open('dependency.json') as f:
  		meta = json.load(f)
  	l=meta['service']['dependency']
  	for item in l:
  		ip=meta['service'][item]['ip']
  		port=meta['service'][item]['ip']
  		print("[Starting ",item," ]"," on ip ",ip," port ",port)
 