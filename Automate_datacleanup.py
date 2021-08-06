#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

from openpyxl import load_workbook

df = pd.read_csv('/Users/ag/Documents/Python_Projects/Clean_up_data/Accounts_opportunities.csv')
print(df.head())


# In[7]:


df.dropna(inplace = True, how='all') #drop all the rows that has all NAN
print(df)


# In[9]:


cleaned_data = df
file_path = '/Users/ag/Documents/Python_Projects/clean_up_data/cleaned_data.xlsx'
cleaned_data.to_excel(file_path, sheet_name = 'cleaned_data', startrow=3)


# In[10]:


wb = load_workbook(file_path)
sheet1 = wb['cleaned_data'] 


# In[11]:


wb.save(filename = file_path)


# In[ ]:




