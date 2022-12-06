#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : Fierce Bird//ZiyahVirani ")
print("Project Name :  COVID DATA ANALYSIS")
print("This is a CSV of more than 200 rows which has Covide data.")
print("The task is to find out top 5 the countries who are least affected by covid")
print("Another task is to find out top 5 the countries who has the maximum number of deaths")
print("Another task is to find out top 5 the countries who has the maximum number of active cases")


# In[20]:


#Covide Data 
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt


dataframe = pd.read_csv('covid19.csv')
df = dataframe.dropna()
df


# In[33]:


#Task 1 
#Sort the data as per total number of cases
sorted_df = df.sort_values(by=['total_cases'])
print(sorted_df)


# In[29]:


#Task 2
#Get top 5 countries who has the least number of cases and plot a bar graph
lowest_cases = sorted_df['total_cases'].head(5)

country = sorted_df['country'].head(5)

name = country
weight = lowest_cases

plt.xlabel("COUNTRY")
plt.xticks(rotation="vertical")
plt.ylabel("TOTAL CASES")

label =name
value = weight
plt.bar(label,value,width=0.4,color=("red","orange","yellow","pink","purple"))


# In[32]:


#Task 3
#Sort the data as per total number of deaths
sorted_death_df = df.sort_values(by=['total_deaths'])
print(sorted_death_df)


# In[34]:


#Task 4
#Get top 5 countries who has the maximum number of deaths and plot a bar graph
highest_deaths = sorted_death_df['total_deaths'].tail(5)
print(highest_deaths)

country = sorted_death_df['country'].tail(5)
print(country)

name = country
weight = highest_deaths

plt.xlabel("COUNTRY")
plt.xticks(rotation="vertical")
plt.ylabel("TOTAL DEATHS")

label =name
value = weight
plt.bar(label,value,width=0.4,color=("red","orange","yellow","pink","purple"))


# In[42]:


#Task 5
#Sort the data as per active cases
sorted_active= df.sort_values(by=['active_cases'])
print(sorted_active)

#Task 6
#Get top 5 countries who has the maximum number of active cases and plot a bar graph
highest_deaths = sorted_active['active_cases'].tail(5)
print(highest_deaths)

country = sorted_active['country'].tail(5)
print(country)

name = country
weight = highest_deaths

plt.xlabel("COUNTRY")
plt.xticks(rotation="vertical")
plt.ylabel("ACTIVE CASES")

label =name
value = weight
plt.bar(label,value,width=0.4,color=("red","orange","yellow","pink","purple"))


# In[41]:





# In[ ]:





# In[ ]:




