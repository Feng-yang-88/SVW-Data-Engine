#!/usr/bin/env python
# coding: utf-8

# In[5]:


#汽车投诉信息
import pandas as pd
result = pd.read_csv('D:\SVW Data Engine\L1\car_data_analyze\car_complain.csv')
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result.columns)
tags = result.columns[7:]


# In[8]:


df= result.groupby(['brand'])['id'].agg(['count'])
df2= result.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
df2.reset_index(inplace=True)
df2= df2.sort_values('count', ascending=False)
print(df2)
query = ('A11', 'sum')
print(df2.sort_values(query, ascending=False))


# In[ ]:





# In[ ]:




