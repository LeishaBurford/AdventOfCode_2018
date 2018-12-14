#!/usr/bin/python3
# -*- coding: utf-8 -*-
# part 1
with open('input.txt') as f:
    guardRecords = f.read().splitlines()

# sort the data by datetime
guardRecords.sort(key=lambda x: ''.join(x.split(' ')[0:2]))

def newGuard(record):
    return '#' in record

def getNewGuardId(record):
    return int(record.split(' ')[3][1:])

def guardFellAsleep(record):
    return 'asleep' in record

def currentMinute(record):
    return int(''.join(record.split(' ')[1][3:5]))

def guardWokeUp(record):
    return 'wakes' in record

def updateSleepTime(oldSleepTimes, startMinute, endMinute):
    for time in range(startMinute, endMinute):
        oldSleepTimes[time] += 1
    return oldSleepTimes

sleeptimes = {}
currentGuard = 0
sleepStartTime = 0
for record in guardRecords:
    # get the id for the guard this corresponds to 
    # find the time they are asleep
    # find the time they are awake
    if (newGuard(record)):
        currentGuard = getNewGuardId(record)
        if currentGuard not in sleeptimes:
            sleeptimes[currentGuard] = [0 for i in range(60)]
    elif (guardFellAsleep(record)): 
        sleepStartTime = currentMinute(record)
    elif (guardWokeUp(record)):  
        sleeptimes[currentGuard] = updateSleepTime(sleeptimes[currentGuard], sleepStartTime, currentMinute(record))

# for sleepRecord in sleeptimes:
#    print(sleepRecord)
#    print(sleeptimes[sleepRecord])

# find sleepiest guard -- I'm sure there's a better way to do this
recordSleepTime = 0
sleepiestGuard = 0
for guard in sleeptimes:
    sleepMinutes = sum(sleeptimes[guard])
    if sleepMinutes > recordSleepTime:
        recordSleepTime = sleepMinutes
        sleepiestGuard = guard

sleepiestMinute = sleeptimes[sleepiestGuard].index(max(sleeptimes[sleepiestGuard]))
print("guard", sleepiestGuard)
print("minute", sleepiestMinute)
print(sleepiestGuard * sleepiestMinute)

# part 2
recordSleepiestMinute = 0
sleepiestGuard = 0
for guard in sleeptimes:
    sleepiestMinute = max(sleeptimes[guard])
    if sleepiestMinute > recordSleepiestMinute:
        recordSleepiestMinute = sleepiestMinute
        sleepiestGuard = guard
    
sleepiestMinute = sleeptimes[sleepiestGuard].index(recordSleepiestMinute)
print("guard", sleepiestGuard)
print("minute", sleepiestMinute)
print(sleepiestGuard * sleepiestMinute)