#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world")


# In[5]:


import sys
print("python version")
print(sys.version)
print("python info")
print(sys.version_info)


# In[6]:


import datetime
now=datetime.datetime.now()
print("current date and time")
print(now.strftime("%y-%m-%d %H:%M:%S"))


# In[7]:


import math
radius = float(input("Enter the radius of the circle :"))

area = math.pi * radius * radius

print("Area of the circle is : {0}".format(area))


# In[ ]:


first_name = input("zahra")
last_name = input("mughal")
print("Hello " + mughal + " " + zahra)


# In[ ]:


num1 = input("10")
num2 = input("20")

sum = float(10) + float(20)

print("sum of {10} and {20} is {30}".format(10,20, sum))


# In[ ]:




