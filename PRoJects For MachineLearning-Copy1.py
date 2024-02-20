#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
cars=pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\cars.csv")
print(cars)


# In[9]:


cars.head()


# In[11]:


cars.shape


# # Data  cleaning

# In[12]:


cars.isnull()


# In[13]:


cars.isnull().sum()


# # If Null value then cars['hp'].fillna(car['hp'].mean(),inplace=True)

# In[14]:


cars


# In[15]:


cars.head(2)


# In[21]:


cars['Unnamed: 0'].value_counts()


# In[23]:


cars.head(2)


# In[25]:


cars[cars['gear'].isin([4,8])]


# In[26]:


cars[cars['disp']>150]


# In[32]:


cars[~(cars['disp']>150)]


# In[31]:


cars.shape


# In[33]:


cars.head()


# In[36]:


cars['hp']=cars['hp'].apply(lambda x:x+3)


# In[37]:


cars


# POLICE DATASETS

# In[1]:


import pandas as pd


# In[2]:


police=pd.read_csv(r"C:\Users\Hp\Downloads\police_shootings.csv")
print(police)


# In[5]:


police.head()


# In[7]:


police.isnull()


# In[11]:


police.isnull().sum()


# In[10]:


police.head()


# In[18]:


data=police[['Person.Name','Person.Gender']]
print(data)


# In[19]:


police['Person.Age'].mean()


# In[ ]:





# In[ ]:




