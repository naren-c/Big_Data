#!/usr/bin/env python3
import json
import sys
from datetime import *
def checkConditions(data):
	if(data["location"] =="nan" and data["sensor_id"]=="nan" and data["humidity"]=="nan" and data["temperature"]=="nan" and data["pressure"]=="nan"):
		return False
	if(data["location"]<2500 and data["location"]>1700 and data["sensor_id"]<5000 and data["humidity"]>=72.00 and data["temperature"]>=12.00 and data["pressure"]>=93500.00):
		return True 

for line in sys.stdin:
	data = json.loads(line.strip())
	if checkConditions(data):
		start_date=data["timestamp"]
		start_date = datetime.strptime(start_date, "%Y-%m-%d")
		print("{:%Y-%m-%d},1".format(start_date))
        

