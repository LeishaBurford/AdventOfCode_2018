#!/usr/bin/env python
# coding: utf-8

# In[49]:


with open('C:\git\AdventOfCode_2018\Day_7\input.txt') as f:
    instructions = f.read().splitlines()


# In[50]:


# part 1
instructions = [(instruction[1], instruction[7]) for instruction in list(map(lambda x: x.split(' '), instructions))]


# In[51]:


instructionRequirements = dict.fromkeys(list(set([y for x, y in instructions])), [])


# In[52]:


# for each requirement, add to dictionary
# sort the dictionary lists
# find an instruction that is not in the requirements -- maybe maintain this in another dictionary

# setup
instructionHasRequirement = dict.fromkeys(list(set([y for x, y in instructions])), False)
for requirement, instruction in instructions:
    print(requirement, instruction)
    instructionRequirements[instruction].append(requirement)
    instructionHasRequirement[instruction] = True
instructionRequirements


# In[ ]:




