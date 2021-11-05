#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = input()

age = int(input())

print("my name is " + name + " my age is " + str(age))


# In[2]:


year = 2021


# In[5]:


Date_of_birth = year - age

Date_of_birth


# In[8]:


Infants: <1
Children: 1-11 years
Teens: 12-17 
Adults: 18-64
Older Adults: 65+


# In[10]:


age = 29
if (age <1): 
  group = "infant"
elif (age >=1) & (age <=11): 
  group = "child"
elif (age >=12) & (age <=17):
  group = "Teen"
elif (age >=18) & (age <=64):
  group = "adult"
else:
  group = "older Adult"
print(group)


# In[11]:


Decade_ago = age - 10

Decade_ago


# In[12]:


for i in range(10, 60, 10):
    print(i)


# In[13]:


new_age = []

new_year = []

for i in range(10, 60, 10): 
  new = age + i
  new_age.append(new)
  print(new_age)

  new_y = year + i 
  new_year.append(new_y)
  print(new_year)


# In[15]:


new_age


# In[16]:


new_year


# In[ ]:


In 2064 you’ll be 13y.o


# In[17]:


len(new_age)


# In[18]:


for i in range(len(new_age)):
  age = new_age[i]
  decade = new_year[i]

  print(" in " + str(decade) + " you'll be " + str(age) + "y.o")


# In[20]:


new_age[0]


# In[ ]:




