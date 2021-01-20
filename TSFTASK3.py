#!/usr/bin/env python
# coding: utf-8

# #  Task -3 Exploratory Data Analysis 

# #### Importing Libraries

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

import warnings 
warnings.filterwarnings('ignore')


# #### Load Dataset

# In[2]:


df=pd.read_csv("C:/Users/user/Downloads/SampleSuperstore.csv")


# ## Some Basic Insights

# In[3]:


df.head() #top 5 rows


# In[4]:


df.info()


# In[5]:


df.corr()


# In[6]:


df.describe()


# In[7]:


df.shape


# In[8]:


df.tail() # last 5 rows


#  ## Number of unique values in each column

# In[9]:


for i in df.columns:
    print(i,len(df[i].unique()))


# ## Check for null values

# In[10]:


df.isnull().sum()


# # Data Visualization

# In[11]:


sns.pairplot(df)


# In[12]:


fig,axes = plt.subplots(1,1,figsize=(12,7))
sns.heatmap(df.corr())
plt.show()


# In[13]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total profit vs Sales")
sns.barplot(data=df.groupby('Sub-Category')['Sales','Profit'].agg(sum), x='Sales',y= 'Profit', ax=axes[1])
df.groupby('Sub-Category')['Sales','Profit'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show


# In[14]:


fig,axes = plt.subplots(1,2,figsize=(14,5))
fig.suptitle("Total Sales vs Quantity")
sns.barplot(data=df.groupby('Sub-Category')['Sales','Quantity'].agg(sum), x='Sales',y= 'Quantity', ax=axes[1])
df.groupby('Sub-Category')['Sales','Quantity'].agg(sum).plot(kind='bar',ax=axes[0])
plt.xticks(rotation=90)
plt.show


# In[20]:


fig,axes=plt.subplots(2,2, figsize=(16,8))
fig.suptitle("Sales with different shipping modes and Segments", fontsize=14)
sns.barplot(df['Ship Mode'], df['Sales'],ax=axes[0,0])
sns.lineplot(df['Ship Mode'], df['Sales'],ax=axes[0,1])
sns.barplot(df['Ship Mode'], df['Sales'],ax=axes[1,0])
sns.lineplot(df['Ship Mode'], df['Sales'],ax=axes[1,1])
plt.show()


# In[22]:


fig,ax=plt.subplots(1,1,figsize=(12,7))
sns.countplot(df['Quantity'],hue=df['Region'])
plt.show


# ## Keynote

# ### 1) The maximum quantity of product in demand was is range 2-4.
# ### 2) Mode of shipping has no effect on sales
# ### 3) West region usually orders 2 or 3 quantites of a good.

# In[ ]:




