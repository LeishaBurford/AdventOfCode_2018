#!/usr/bin/python3

with open('testinput.txt') as f:
    instructions = f.read().splitlines()

# part 1

instructions = [(instruction[1], instruction[7])
                for instruction in list(map(lambda x: x.split(' '), instructions))]
instructionRequirements = {instruction: []
                           for instruction in list(set([y for x, y in instructions]))}
# setup
instructionHasRequirement = {x : False for x in list(set([x for x, y in instructions]))}

for requirement, instruction in instructions:
    instructionRequirements[instruction].append(requirement)
    instructionHasRequirement[instruction] = True

ready = sorted([instruction for instruction in instructionHasRequirement.keys() if not instructionHasRequirement[instruction]], reverse=True)
for instruction in ready:
    if not instructionHasRequirement:
        instructionHasRequirement.pop(instruction)

result = ''
while(ready):
    newInstruction = ready.pop()
    instructionHasRequirement.pop(newInstruction)
    result += newInstruction
    # update instruction requirements
    for instruction in instructionRequirements:
        if newInstruction in instructionRequirements[instruction]:
            instructionRequirements[instruction].remove(newInstruction)
            # if req's list is now empty, update the bool
            instructionHasRequirement[instruction] = True if instructionRequirements[instruction] else False
    
    ready += sorted([instruction for instruction in instructionHasRequirement if not instructionHasRequirement[instruction] and instruction not in ready], reverse=True)
print(result)

# part 2
instructionRequirements = {instruction: []
                           for instruction in list(set([y for x, y in instructions]))}
# setup
instructionHasRequirement = {x : False for x in list(set([x for x, y in instructions]))}

for requirement, instruction in instructions:
    instructionRequirements[instruction].append(requirement)
    instructionHasRequirement[instruction] = True

ready = sorted([instruction for instruction in instructionHasRequirement.keys() if not instructionHasRequirement[instruction]], reverse=True)
for instruction in ready:
    if not instructionHasRequirement:
        instructionHasRequirement.pop(newInstruction)

result = ''
workers = {x : [-1, ''] for x in range(2)}
timePassed = 0
while(ready):
    # assign instruction to worker
    print('current workers', workers)
    if -1 in workers.values():
        newInstruction = ready.pop()
        instructionHasRequirement.pop(newInstruction)
        worker = [y[0] for x, y in workers if y[0] == -1][0]
        # set the time
        workers[worker] = [ord(newInstruction) - 64, newInstruction]
        print('new isntruction', workers)
    # if worker is done
    doneInstrcutions = sorted([workers[x][1] for x in workers if workers[x][0] == 0], reverse=True)
    print('doneInstructions', doneInstrcutions)
    if doneInstrcutions:
        result += doneInstrcutions
        # update instruction requirements
        for instruction in instructionRequirements:
            if newInstruction in instructionRequirements[instruction]:
                instructionRequirements[instruction].remove(newInstruction)
                # if req's list is now empty, update the bool
                instructionHasRequirement[instruction] = True if instructionRequirements[instruction] else False
        ready += sorted([instruction for instruction in instructionHasRequirement if not instructionHasRequirement[instruction] and instruction not in ready], reverse=True)
    for worker in workers:
        workers[worker][0] -= 1
        print('updated workesr', workers)
    timePassed += 1
print(timePassed)
