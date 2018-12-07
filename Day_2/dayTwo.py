#!/usr/bin/env python

# part 1
with open('c:\git\AdventOfCode_2018\Day_2\input.txt') as f:
    boxIds = f.read().splitlines()

twoOfALetter = 0
threeOfALetter = 0

for boxId in boxIds:
    temp = {}
    for char in boxId:
        if (char in temp):
            temp[char] += 1
        else:
            temp[char] = 1
    twoOfALetter = twoOfALetter + 1 if 2 in temp.values() else twoOfALetter
    threeOfALetter = threeOfALetter + 1 if 3 in temp.values() else threeOfALetter

print(twoOfALetter * threeOfALetter)

# part 2

# we are assuming the strings are of equal length here
def differByOneChar(a, b):
    totalDifferences = 0
    for i in range(len(a)):
        totalDifferences = totalDifferences + 1 if a[i] != b[i] else totalDifferences
    return totalDifferences == 1    
        
def sharedCharacters(a, b):
    characters = ''
    for i in range(len(a)):
        characters = characters + a[i] if a[i] == b[i] else characters
    return characters
    
for i in range(len(boxIds) - 1):
    for j in range(i, len(boxIds)):
        if (differByOneChar(boxIds[i], boxIds[j])):
            print(sharedCharacters(boxIds[i], boxIds[j]))
            
            