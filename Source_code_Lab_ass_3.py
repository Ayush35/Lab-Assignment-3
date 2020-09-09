#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = ['abc','xyz','aba','1221']
num=0
for i in list:
    if len(i)>1 and i[0] == i[-1] :
        num= num+1

print(num) 


# In[ ]:




