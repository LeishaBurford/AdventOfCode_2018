#!/usr/local/bin/python3

with open('testinput.txt') as f:
    coordinates = f.read().splitlines()

def computeDistance(a,b,c,d):
	return abs(a - c) + abs(b - d)
coordinates = [coordinate.split(',') for coordinate in coordinates ]
coordinates = list(map(lambda x: (list(map (lambda y: int(y ) - 1, x) )), coordinates))
# x for xy in coor 
xRange = [min([x for x, y in coordinates]), max([x for x, y in coordinates])]
yRange = [min([y for x , y in coordinates]), max([y for x, y in coordinates])]


grid = [[-1 for i in range(xRange[0], xRange[1] + 2)] for j in range(yRange[0], yRange[1] + 2)]
print(xRange, yRange)

# for row in grid:
# 	print(row)

# add the coordinates
val = 0
for c in coordinates:
	grid[c[1]][c[0]] = val
	val += 1

names = [i for i in range(val + 1)]
for row in grid:
	print(row)

closestPoints = dict.fromkeys(names)

for point in closestPoints:
	closestPoints[point] = 0

for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == -1:
			minDistance = 10000
			val = 0
			for c in coordinates:
				distance = computeDistance(c[0], c[1], x, y)
				if distance < minDistance:
					minDistance = distance
					closestPoints[val] += 1
				val += 1

print(min(closestPoints.values()))

























