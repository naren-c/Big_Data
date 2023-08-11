#!/usr/bin/env python3
import json
import sys
from datetime import *
import math
def euclideanDistance(latitude,longitude,d_lat,d_lon):
	return math.dist([latitude,longitude],[d_lat,d_lon])
d=float(sys.argv[0])	
latitude=float(sys.argv[1])
longitude=float(sys.argv[2])
for line in sys.stdin:
	record=json.loads(line.strip())
	d_lat=record["lat"]
	d_lon=record["lon"]	
	if str(d_lat)!="NaN" and str(d_lon)!="NaN":
		coordinates={"latitude":d_lat,"longitude":d_lon}
		distance=euclideanDistance(latitude,longitude,d_lat,d_lon)
		if(distance <=d and record["humidity"]>48.00 and record["humidity"]<54.00 and record["temperature"]>20.00 and record["temperature"]<24.00):
			start_date=record["timestamp"]
			start_date = datetime.strptime(start_date, "%Y-%m-%d")
			print("{:%Y-%m-%d},1".format(start_date))
	
	
	
	
	
	
	
	

