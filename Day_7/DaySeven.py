#!/usr/bin/env python
# coding: utf-8

# In[138]:


with open('C:\git\AdventOfCode_2018\Day_7\input.txt') as f:
    instructions = f.read().splitlines()


# In[139]:


# part 1
instructions = [(instruction[1], instruction[7]) for instruction in list(map(lambda x: x.split(' '), instructions))]


# In[140]:


instructionRequirements = { instruction : [] for instruction in list(set([y for x, y in instructions])) }


# In[141]:


# for each requirement, add to dictionary
# sort the dictionary lists
# find an instruction that is not in the requirements -- maybe maintain this in another dictionary

# setup
instructionHasRequirement = dict.fromkeys(list(set([x for x, y in instructions])), False)

for requirement, instruction in instructions:
    instructionRequirements[instruction].append(requirement)
    instructionHasRequirement[instruction] = True
instructionRequirements

ready = [instruction for instruction in instructionHasRequirement.keys() if not instructionHasRequirement[instruction]].sort()
result = ''
while(ready):
    newInstruction = ready.pop()
    result += newInstruction
    # update instruction requirements
    for instruction in instructionRequirements:
        if newInstruction in instructionRequirements[instruction]:
            instructionRequirements[instruction].remove(newInstruction)
            # if req's list is now empty, update the bool
            instructionHasRequirement[instruction] = False if not instructionHasRequirement[instruction] else True
            



