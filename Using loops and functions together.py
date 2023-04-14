#!/usr/bin/env python
# coding: utf-8

# In[17]:


salaries = [1000,2000,3000,4000,5000]
salaries[0]*20/100 + salaries[0]
salaries[1]*20/100 + salaries[1]
salaries[2]*20/100 + salaries[2]
#We see that there is a repeating pattern.
#We need to write a function using a loop.

def new_salary(x):
    print(x*20/100 + x)

new_salary(1000)
new_salary(2000)

for x in salaries:
    new_salary(x)


#If we want to raise 10% for those whose salary is equal to or higher than 3000
#20% for those whose salary is less than 3000

def salary_high(x):
    print(x*10/100 + x)
def salary_low(x):
    print(x*20/100 + x)

for i in salaries:
    if i >= 3000:
        salary_high(i)
    else:
        salary_low(i)

