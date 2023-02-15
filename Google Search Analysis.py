#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytrends


# In[2]:


import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()


# In[3]:


trends.build_payload(kw_list=["Google Search Analysis"])
data = trends.interest_by_region()
data = data.sort_values(by="Google Search Analysis",ascending=False)
data = data.head(10)
print(data)


# In[4]:


data.reset_index().plot(x="geoName",y="Google Search Analysis",figsize=(15,12),kind="bar")
plt.style.use('fivethirtyeight')
plt.show()


# In[5]:


data = TrendReq(hl='en-US',tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()

