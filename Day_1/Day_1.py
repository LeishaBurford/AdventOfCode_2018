#!/usr/bin/env python
# coding: utf-8

# In[1]:



with open('C:\git\AdventOfCode_2018\Day_1\input.txt') as f:
    frequencies = f.read().splitlines()


# In[4]:


def IsPositive(char):
    return char == '+'


# In[ ]:





# In[10]:


frequenciesAsIntegers = [int(value[1:]) if IsPositive(value[0]) else int(value[1:]) * -1 for value in frequencies]


# In[ ]:





# In[11]:


print(frequenciesAsIntegers)


# In[ ]:




