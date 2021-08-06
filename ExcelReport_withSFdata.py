#!/usr/bin/env python
# coding: utf-8

# In[121]:


import pandas as pd

report = pd.read_csv('/Users/ag/Documents/Python_Projects/Clean_up_data/Accounts_opportunities.csv',header=8)

report.dropna(inplace = True, how='all') #drop all the rows that has all NAN

report.drop(index=report.index[-4:], 
        axis=0, 
        inplace=True)

report.rename({"Unnamed: 1":"a"}, axis="columns", inplace=True) #delete the column called "Unnamed: 1"

report.drop(["a"], axis=1, inplace=True)

report2=report.drop_duplicates(subset=['Account Number']) #delete duplicates by looking at the account number only and saving it in a different variable

# to export the data: report.to_csv("output.csv")
report2.to_csv("output2.csv")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


x =['New Customer', 'Existing Customer Upgrade']

y = [6,3]

fig, ax = plt.subplots(figsize =(16, 2))



report2['Type'].value_counts().plot(kind='bar',color=['orange','blue'],figsize=(7, 5),rot=0)
plt.title('Type of Customers')
plt.xlabel('Type')
plt.ylabel('Count')

for index, value in enumerate(y):
    plt.text(index,value, str(value))
plt.show()

#Total per type of customers
#len(report2[report2['Type'] == 'New Customer'])


#len(report2[report2['Type'] == 'Existing Customer - Upgrade'])


#Opp count by Country

report2["Billing Country"].value_counts().plot(
    kind="bar", stacked=True
).legend(
    loc='upper right', ncol=4, title="Opp by Country")

#stack bar"

report2.groupby(['Billing Country', 'Type']).size().unstack().plot.bar(stacked=True)

plt.show()

    


# In[122]:


my_labels='No', 'Yes'
my_colors = ['lightblue', 'silver']
plt.pie(report['Won'].value_counts(),labels=my_labels,autopct='%1.1f%%',colors=my_colors)
plt.title('Percentage of Opp Won vs Lost')

plt.show()


# In[107]:


report['Won'].value_counts()


# In[ ]:




