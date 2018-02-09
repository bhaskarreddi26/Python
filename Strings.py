
# coding: utf-8

# In[4]:


s = 'shak#spea#e'
c = 'a'
print ([pos for pos, char in enumerate(s) if char == c])


# In[13]:


def comp1(s, c):
    for x, y in zip(s, c):
        if x == y:
            print(list[x])


# In[14]:


s = 'shak#spea#e'
c = 'ak'
comp1(s, c)


# In[22]:


s = 'shak#spea#e'
c = 'k'
print(s.find(c))
print(s.count(c))
print (.join('c'))

