#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


report = pd.read_csv('/Users/ag/Documents/Python_Projects/Clean_up_data/Accounts_opportunities.csv',header=8)


# In[4]:


print(report.head(8))


# In[5]:


print(report.shape)


# In[6]:


print(report)


# In[7]:


report.dropna(inplace = True, how='all') #drop all the rows that has all NAN


# In[8]:


print(report)


# In[9]:


report.drop(index=report.index[-4:], 
        axis=0, 
        inplace=True)


# In[10]:


report.rename({"Unnamed: 1":"a"}, axis="columns", inplace=True) #delete the column called "Unnamed: 1"


# In[11]:


report.drop(["a"], axis=1, inplace=True)


# In[12]:


print(report)


# In[13]:


report.duplicated()


# In[14]:


print(report)


# In[15]:


report


# In[16]:


report.drop_duplicates()


# In[23]:


report2=report.drop_duplicates(subset=['Account Number']) #delete duplicates by looking at the account number only and saving it in a different variable


# In[24]:


report2


# In[26]:


# to export the data: report.to_csv("output.csv")
report
report2.to_csv("output2.csv")


# In[ ]:




