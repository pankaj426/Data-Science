#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("Book1.csv")


# In[ ]:


df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[6]:


df[df.Temperature==50]


# In[7]:


df[df.Temperature ==df['Temperature'].max()]


# In[14]:


df[df.Temperature ==df['Temperature'].max()]


# In[16]:


df['Events'][df.Temperature ==df['Temperature'].max()]


# In[17]:


df.index


# In[19]:


df.set_index('EST', inplace=True)
df


# In[22]:


df.loc['1/27/2016']


# In[23]:


df.reset_index(inplace=True)


# In[24]:


df


# In[ ]:




