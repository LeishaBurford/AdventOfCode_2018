#!/usr/local/bin/python3

with open('input.txt') as f:
    coordinates = f.read().splitlines()

coordinates = [coordinate.split(',') for coordinate in coordinates ]
coordinates = list(map(lambda x: (list(map (lambda y: int(y), x) )), a))

xRange = tuple(min([coordinate[0] for coordinate in coordinates]), max([coordinate[0] for coordinate in coordinates]))
yRange = tuple(min([coordinate[1] for coordinate in coordinates]), max([coordinate[1] for coordinate in coordinates]))

print(coordinates)