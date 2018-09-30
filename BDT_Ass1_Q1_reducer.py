#! /usr/bin/python

import sys

abc = {}
allNums = []
lastKey = None
for line in sys.stdin:
    splitline=line.strip().split()
    if len(splitline)!=2:
        continue
    curKey, curNum = splitline
    if lastKey:
		if lastKey != curKey:
			abc[lastKey] = allNums
			allNums = []
    lastKey = curKey
    allNums = allNums +  [int(curNum)]
if lastKey!= None:
    abc[lastKey] = allNums
for x in abc.keys():
	print(x,min(abc[x])) 