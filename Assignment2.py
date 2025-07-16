
# coding: utf-8

# # ASSIGNMENT 2:

# In[ ]:


Task 1: Check if a Number is Even or Odd.


# In[8]:


num = int(input('Enter a number'))
#num2 = int(input('Enter second number'))

if num/2==0:
    print(num,"It's even number.")
    
else:
    print(num,'This is odd number.')
   


# In[ ]:


Task 2: Sum of Integers from 1 to 50 Using a Loop.


# In[25]:


total = 0
for i in range(1, 51):
    total += i

print("The sum of numbers from 1 to 50 is:", total)

