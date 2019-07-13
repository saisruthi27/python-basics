#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2. Draw a Spirling Square with Pen color as 'Red'.
import turtle as t
a1= t.Turtle()
a1.pencolor('red')
for i in range(40):
    a1.forward(i*10)
    a1.right(90)
t.done()


# In[4]:


#3. Write a python programming to print the large digit from given number
#Example:-
#Test cases:- Input:- 195263 Output:- 9
#Test cases:- Input:- 36372  Output:- 7
def printlarge(n):
    large=0
    while n!=0:
        r=n%10
        if large<r:
            large=r
        n=n//10
    return large
print(printlarge(19528))
print(printlarge(36372))


# In[3]:


# TO PRINT PALINDROME COUNT BETWEEN TWO NUMBERS
def ispalindrome(n):
    rev=0
    buffer=n
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==buffer:
         return True
    else:
        return False
    return
def countpalindrome(lb,ub):
    cnt=0
    while lb!=ub:
        if ispalindrome(lb)==True:
            cnt=cnt+1
        lb=lb+1
    return cnt
print(countpalindrome(1,10))
print(countpalindrome(11,100))


# In[ ]:





# In[ ]:





# In[ ]:




