with open('input.txt') as f:
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

val = 0
for x, y in coordinates:
    grid[y][x] = val
    val += 1
names = [i for i in range(val)]
coordinateIndex = dict(zip(names, coordinates))
closestPoints = dict.fromkeys(names, 0)

infinitePoints = []


def determineClosestPoint(x, y, points):
    distances = [computeDistance(x, y, c[0], c[1]) for c in points]
    # if equally close to 2+ points, return -1
    return distances.index(min(distances)) if distances.count(min(distances)) == 1 else -1


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

print(max([closestPoints[closestPoint]
           for closestPoint in closestPoints if closestPoint not in infinitePoints]))

# part 2
xMax = max(list(zip(*coordinates))[0])
xMin = min(list(zip(*coordinates))[0])
yMax = max(list(zip(*coordinates))[1])
yMin = min(list(zip(*coordinates))[1])

locations = [(x, y) for x in range(xMin, xMax) for y in range(yMin, yMax)]
grandTotal = 0

for location in locations:
	grandTotal += 1 if sum([computeDistance(location[0], location[1], c[0], c[1]) for c in coordinates]) < 10000 else 0

print(grandTotal)
# refactoring

# with open('C:/git/AdventOfCode_2018/Day_6/testinput.txt') as f:
#     coordinates = f.read().splitlines()


# coordinates = [coordinate.split(',') for coordinate in coordinates]
# coordinates = list(
#     map(lambda x: (list(map(lambda y: int(y) - 1, x))), coordinates))
# xMax = max(list(zip(*coordinates))[0])
# yMax = max(list(zip(*coordinates))[1])

# def computeDistances(location, coordinates):
#     return [computeDistance(location, c) for c in coordinates]

# def computeDistance(p, q):
#     return abs(p[0] - q[0]) + abs(p[1] - q[1])

# locations = [(x, y) for x in range(xMax) for y in range(yMax)]
# # store the locations that are equally far from two or more coordinates
# equiDistant = [(x, y) for x, y in [location for location in locations if computeDistances(location, coordinates).count(min(computeDistances(location, coordinates))) > 1]]
