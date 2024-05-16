#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd 
import matplotlib.pyplot as plt 


# In[35]:


get_ipython().system('dir mtc*')


# In[36]:


cd


# In[28]:


pd.read_csv("mtcars.csv")


# In[29]:





# In[10]:


df=pd.read_csv("mtcars.csv")


# In[11]:


mtcars.head()


# In[12]:


mtcars.tail()


# In[13]:


df.shape


# In[14]:


mtcars.describe()


# In[16]:


df.info()


# In[17]:


mtcars.columns


# In[24]:


mtcars = pd.read_csv("mtcars.csv") 
plt.hist(mtcars['mpg'], bins=10, color='yellow', edgecolor='black') 
plt.xlabel('Miles per gallon (mpg)') 
plt.ylabel('Frequency') 
plt.title('Histogram of Miles per gallon (mpg)')
plt.show()


# In[ ]:




