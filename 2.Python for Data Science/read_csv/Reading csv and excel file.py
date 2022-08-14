#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pandas library

import pandas as pd


# In[2]:


# Reading the csv file

df = pd.read_csv("data.csv")


# In[3]:


df.head()


# In[4]:


# Reading excel file

df1 = pd.read_excel("data.xlsx")


# In[5]:


df1.head()

