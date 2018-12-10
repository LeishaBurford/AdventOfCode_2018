#!/usr/bin/env python

# part 1
with open('c:\git\AdventOfCode_2018\Day_4\input.txt') as f:
    guardRecords = f.read().splitlines()

# sort set of data by
guardRecords = [a for a in guardRecords if a != 'ÿþ']
before = len(guardRecords)
guardRecords.sort(key=lambda x: x.split(' ')[0])

for record in guardRecords:
    print(record)