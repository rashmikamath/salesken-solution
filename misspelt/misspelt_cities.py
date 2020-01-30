#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[102]:


cities = pd.read_csv("Correct_cities.csv")

cities.shape

# In[103]:


cities['name'] = cities['name'].apply(lambda x:x.lower())


# In[104]:


cities = cities.sort_values(by =['country', 'name'])

cities.country.nunique()

# In[105]:


cities.head(10)

# In[106]:


missplet = pd.read_csv("Misspelt_cities.csv")

missplet.head()

# In[107]:


missplet['misspelt_name'] = missplet['misspelt_name'].apply(lambda x:x.lower())


# In[108]:


missplet = missplet.sort_values(by =['country', 'misspelt_name'])


# In[109]:


missplet.head(10)


# In[110]:

final_df = pd.merge(cities,missplet,on='country',how="outer")


# In[111]:


# In[125]:


final_df = final_df.fillna('')


# In[126]:


final_df


# In[128]:


type(final_df['misspelt_name'][0])


# In[129]:

def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    lensum = float(m + n)
    d = []           
    for i in range(m+1):
        d.append([i])        
    del d[0][0]    
    for j in range(n+1):
        d[0].append(j)       
    for j in range(1,n+1):
        for i in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                d[i].insert(j,d[i-1][j-1])           
            else:
                minimum = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+2)         
                d[i].insert(j, minimum)
    ldist = d[-1][-1]
    ratio = (lensum - ldist)/lensum
    return ratio

final_df['ratio'] = final_df.apply(lambda x:levenshteinDistance(x['name'], x['misspelt_name']),axis=1)


# In[ ]:

correct = final_df[final_df['ratio']==1]

incorrect = final_df[(final_df['ratio'] >=0.75) & (final_df['ratio'] <=0.99 )]


# This list contains all the unique ids that are misspelt
unique_mispelt_id = list(set(incorrect.id))

print("Printing Misspelt city ids")
for uid in unique_mispelt_id:
	print(uid)



# In[ ]:




