#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sum =0
enter_number =int(input())
a=0

while a<=enter_number:
    sum=sum+a
    a=a+1
print(sum)    
    


# In[ ]:


a=int(input())
c=True
for b in range(2,a//2):
    if a%b==0:
        print("not prime")
        c=False
        break
if c==True:
    print("prime") 
       

