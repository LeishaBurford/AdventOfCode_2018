#!/usr/bin/env python
# coding: utf-8

# In[2]:


# part 1
with open('C:\git\AdventOfCode_2018\Day_1\input.txt') as f:
    inputData = f.read().splitlines()


# In[3]:


def IsPositive(char):
    return char == '+'


# In[7]:


frequencies = [int(value[1:]) if IsPositive(value[0]) else int(value[1:]) * -1 for value in inputData]
print(sum(frequencies))


# In[ ]:


# part 2


# In[20]:


encounteredFrequencies = {}
currentFrequency = 0
foundDuplicate = False
while not foundDuplicate:
    for value in frequencies:
        currentFrequency += value
        if (currentFrequency in encounteredFrequencies):
            print(currentFrequency)
            foundDuplicate = True
            break
        encounteredFrequencies[currentFrequency] = 1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




