with open('./testinput.txt') as f:
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

names = [i for i in range(val)]
for row in grid:
	print(row)

coordinateIndex = dict(zip(names, coordinates))
#print(closestPoints)

closestPoints = dict.fromkeys(names, 0)

def determineClosestPoint(x, y, points):
    #miValue=  10000
    #or c in points:
        
    return [computeDistance(x, y, c[0], c[1]) for c in points].index(min([computeDistance(x, y, c[0], c[1]) for c in points]))

for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == -1:
			closestPoint = determineClosestPoint(x, y, coordinates)
			closestPoints[closestPoint] += 1
        else:
            closestPoints[grid[y][x]] += 1
            

print(min(closestPoints.values()))
print(closestPoints.values())
