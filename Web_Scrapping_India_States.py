#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install requests')
get_ipython().system('pip install beautifulsoup4')


# In[7]:


from bs4 import BeautifulSoup
#import requests library
import requests
#the website URL
url_link = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"
result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

print(doc.prettify())


# In[8]:


# FIND ELEMENTS BY ID:


# In[9]:


res = doc.find(id = "content")
print(res)


# In[10]:


#FIND ELEMENTS BY CLASS NAME:


# In[11]:


heading = res.find(class_ = "firstHeading")
print(heading)


# In[12]:


#EXTRACTING TEXT FROM HTML ELEMENTS


# In[13]:


print(heading.text)


# In[14]:


#SEARCHING USING STRING(TEXT):


# In[15]:


res = doc.find_all(text = "Maharashtra")
print(res)


# In[16]:


#SEARCH BY PASSING A LIST


# In[18]:


res=doc.find_all(["a","p","div"])
res


# In[19]:


#SEARCH USING A REGULAR EXPRESSION


# In[20]:


import re

for str in doc.find_all(text = re.compile("1947")):
  print(str)


# In[21]:


for str in doc.find_all(text = re.compile("1947"), limit = 4):
  print(str)


# In[22]:


print(doc.select("title"))


# In[23]:


print(doc.select("html head title"))


# In[59]:


my_table=doc.find("table", class_="wikitable sortable plainrowheaders")


# In[37]:


th_tags = my_table.find_all('th')
names = []

for elem in th_tags:
    # finding the <a> tag
    a_links = elem.find_all("a")
    
    # getting the text inside the <a> tag
    for i in a_links:
        names.append(i.string)

print(names)


# In[38]:


final_list = names[8: ]
states = []
for str in final_list:
  if len(str) > 3:
   states.append(str)
print(states)


# In[88]:


Vehicle_codes = []
for row in my_table.find_all('tr')[1:]:  # Skipping the header row
        cells = row.find_all('td')
        Vehicle_codes.append(cells[1].text.strip())  

print(Vehicle_codes)



# In[89]:


Population = []
for row in my_table.find_all('tr')[1:]:  # Skipping the header row
        cells = row.find_all('td')
        Population.append(cells[6].text.strip())  

print(Population)


# In[95]:


import pandas as pd

df = pd.DataFrame()

df['Vehicle_codes'] = Vehicle_codes
df['Population'] = Population

print(df)


# In[96]:


df.to_csv('Vehicle_code_info.csv')


# In[ ]:




