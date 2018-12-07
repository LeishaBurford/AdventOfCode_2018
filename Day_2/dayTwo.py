#!/usr/bin/env python

# part 1
with open('input.txt') as f:
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
