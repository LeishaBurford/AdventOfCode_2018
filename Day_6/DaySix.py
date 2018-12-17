with open('testinput.txt') as f:
    coordinates = f.read().splitlines()


def computeDistance(a, b, c, d):
    return abs(a - c) + abs(b - d)
coordinates = [coordinate.split(',') for coordinate in coordinates]
coordinates = list(
    map(lambda x: (list(map(lambda y: int(y) - 1, x))), coordinates))
# x for xy in coor
xRange = [min([x for x, y in coordinates]), max([x for x, y in coordinates])]
yRange = [min([y for x, y in coordinates]), max([y for x, y in coordinates])]


grid = [[-1 for i in range(0, xRange[1] + 2)]
        for j in range(0, yRange[1] + 2)]
print(xRange, yRange)
print(len(grid[0]), len(grid))

# for row in grid:
# 	print(row)

# add the coordinates
val = 0
for x, y in coordinates:
    grid[y][x] = val
    val += 1
# for x, y in coordinates:
    # print(x, y)
 #    grid[y][x] = val
 #    val += 1
names = [i for i in range(val)]
coordinateIndex = dict(zip(names, coordinates))
# print(closestPoints)

closestPoints = dict.fromkeys(names, 0)

infinitePoints = []


def determineClosestPoint(x, y, points):
    distances = [computeDistance(x, y, c[0], c[1]) for c in points]
    # if equally close to 2+ points, return -1
    return distances.index(min(distances)) if len(distances) == len(set(distances)) else -1


def isOnEdge(x, y):
    return y in yRange or x in xRange

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == -1:
            closestPoint = determineClosestPoint(x, y, coordinates)
            if closestPoint != -1:
            	grid[y][x] = closestPoint
                closestPoints[closestPoint] += 1
            else:
            	grid[y][x] = 8
            if isOnEdge(x, y):
                infinitePoints.append(closestPoint)
        else:
            closestPoints[grid[y][x]] += 1

for row in grid:
	print(row)

print(closestPoints.values())

print(max([closestPoints[closestPoint]
           for closestPoint in closestPoints if closestPoint not in infinitePoints]))
