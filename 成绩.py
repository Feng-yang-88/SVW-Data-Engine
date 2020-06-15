#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 统计全班成绩
from pandas import Series,DataFrame


# In[2]:


import pandas as pd


# In[3]:


data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}


# In[4]:


df = DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
print(df)


# In[5]:


print('全班平均成绩：')
print(df.mean())


# In[6]:


print('全班各科最低：')
print(df.min())


# In[7]:


print('全班各科最高：')
print(df.max())


# In[8]:


print('方差：')
print(df.var())
print('标准差：')
print(df.std())


# In[10]:


df['sum'] = df.sum(axis=1)
print('总分排名：')
print(df.sort_values(by='sum',ascending = False ))


# In[ ]:




