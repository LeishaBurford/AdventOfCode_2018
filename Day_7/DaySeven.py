#!/usr/bin/python3

with open('testinput.txt') as f:
    instructions = f.read().splitlines()

# part 1
instructions = [(instruction[1], instruction[7])
                for instruction in list(map(lambda x: x.split(' '), instructions))]
instructionRequirements = {instruction: []
                           for instruction in list(set([y for x, y in instructions]))}

# setup
instructionHasRequirement = dict.fromkeys(
    list(set([x for x, y in instructions])), False)

for requirement, instruction in instructions:
    instructionRequirements[instruction].append(requirement)
    instructionHasRequirement[instruction] = True

ready = sorted([instruction for instruction in instructionHasRequirement.keys(
) if not instructionHasRequirement[instruction]], reverse=True)

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
            instructionHasRequirement[
                instruction] = False if not instructionHasRequirement[instruction] else True
    ready += sorted([instruction for instruction in instructionHasRequirement.keys(
    ) if not instructionHasRequirement[instruction]], reverse=True)

print(result)
