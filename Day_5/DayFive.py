#!usr/bin/python3

# part 1
with open('testinput.txt') as f:
    polymers = f.read()


def reactThePolymers(polymers):
    reactedPolymer = polymers
    reactionOccured = True
    while(reactionOccured):
        reactionOccured = False
        for i in range(len(polymers) - 1):
            if abs(ord(polymers[i]) - ord(polymers[i + 1])) == 32:
                # these cancel eachother
                reactionOccured = True
                reactedPolymer = reactedPolymer.replace(polymers[i] + polymers[i + 1], '')
        
        polymers = reactedPolymer
    return polymers

resultingPolymer = reactThePolymers(polymers)
print(len(resultingPolymer))

# part 2

uniquePolymers = set(polymers.lower())
maxPolymerLength = 0
for unit in uniquePolymers:
    polymerLength = len(reactThePolymers(polymers.replace(unit, '').replace(unit.upper(), '')))
    if polymerLength > maxPolymerLength:
        maxPolymerLength = polymerLength

print(maxPolymerLength)
