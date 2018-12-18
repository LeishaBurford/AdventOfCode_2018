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


# In[ ]:




