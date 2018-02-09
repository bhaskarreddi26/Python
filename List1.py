
# coding: utf-8

# In[1]:


import findspark
findspark.init('/home/ubuntu/spark-2.2.1-bin-hadoop2.7')


# In[2]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('test').getOrCreate()


# In[8]:


a = [1,2,1,3,1,2,4]


# In[11]:


data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)


# In[12]:


a = [16, 19, 11, 15, 10, 12, 14]

#repeating loop len(a)(number of elements) number of times
for j in range(len(a)):
    #initially swapped is false
    swapped = False
    i = 0
    while i<len(a)-1:
        #comparing the adjacent elements
        if a[i]>a[i+1]:
            #swapping
            a[i],a[i+1] = a[i+1],a[i]
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break
print (a)


# In[18]:


a = [1,2,3,4,6,1,8]
b = [2,1,2,4,5,6,8]
[i for i, j in zip(a,b) if i ==j]


# In[29]:


mergedlist = a + b


# In[27]:


print ((mergedlist))


# In[30]:


d =  list(zip(a,b))


# In[31]:


print (d)


# In[33]:


f = zip(a,b)
print (tuple(f))

a = [1,2,3,4,5,6,7]
import sys
print ([*filter(lambda x: x >4, a)])

print ([x for x in a if x < 3])

