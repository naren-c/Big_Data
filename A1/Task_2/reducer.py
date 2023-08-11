#!/usr/bin/env python3
import sys

currenttimestamp = None
currentcount = 1
timestamp = None

for row in sys.stdin:

    timestamp, count = row.rsplit(',', 1)
    count = int(count)

    if currenttimestamp is None:
        currenttimestamp = timestamp
        currentcount = count
        continue


    if timestamp == currenttimestamp:
        currentcount += count
    else:
        print(currenttimestamp, currentcount)

        currenttimestamp = timestamp
        currentcount = count

if timestamp == currenttimestamp:
    print(timestamp, currentcount)     
