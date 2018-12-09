#!usr/bin/python3
import re
#part 1
with open('input.txt') as f:
    inputData = f.read().splitlines()

elfClaims = [i.split(' ') for i in [claim.replace('\x00', '').replace('\xff', '').replace('\xfe', '') for claim in inputData ] if i]

def extractCoordinates(a):
    return [int(coordinate) for coordinate in  a.replace(':', '').split(',')]

def extractClaimSize(a):
    return [int(coordinate) for coordinate in a.split('x')]

def extractElfId(a):
    return int(a.replace('#', ''))

# #1 @ 35,93: 11x13 <-- parse this

elfClaims = [ [extractElfId(claim[0]), extractCoordinates(claim[2]), extractClaimSize(claim[3])] for claim in elfClaims]

fabric = [ [0 for i in range(1000)] for j in range(1000)]

for claim in elfClaims:
    for i in range(claim[1][1], claim[1][1] + claim[2][1]):
        for j in range(claim[1][0], claim[1][0] + claim[2][0]):
            fabric[i][j] += 1

overlappingClaims = 0
for row in fabric:
    for inch in row:
        overlappingClaims = overlappingClaims + 1 if inch > 1 else overlappingClaims

print(overlappingClaims)

# part 2
def fabricLocationIsUnclaimed(a):
    return a == 0

elfIdsOverlap = dict.fromkeys([i for i in range(1, len(elfClaims) + 1)])

fabric = [ [0 for i in range(1000)] for j in range(1000)]

for claim in elfClaims:
    for i in range(claim[1][1], claim[1][1] + claim[2][1]):
        for j in range(claim[1][0], claim[1][0] + claim[2][0]):
            if fabricLocationIsUnclaimed(fabric[i][j]):
                fabric[i][j] = claim[0]
            else:
                elfIdsOverlap[claim[0]] = True
                elfIdsOverlap[fabric[i][j]] = True
                fabric[i][j] = claim[0]

for elfId in elfIdsOverlap:
    if not elfIdsOverlap[elfId]:
        print(elfId)

