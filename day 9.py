#!/usr/bin/env python
# coding: utf-8

# In[1]:




lst=[1,8,16,9,2]
print(lst)#access the entire list
print(lst[0])#access first item of list
print(lst[1])#access second item of list
print(lst[0])#access first item of list
print(lst[-1])#access last item of list
print(lst[-2])#access second item of list
print(lst[1:])
print(lst[1:4])


# In[2]:


li=["gitam","python",1989,2002]
print(li)
print(li[0])
print(li[1])
print(li[-1])
print(li[-2])
li[2]=2019
print(li)


# In[3]:


#basic list operations
list1=[1,9,6,18,2]
print(len(list1))
print(list1*2)
print(len(list1)/2)
print(9 in list1)
print(100 in list1)
for x in range(len(list1))
print(list1[x],end=" ")


# In[ ]:


#function of list
a=[1,9,6,18,2]
print(min(a))
print(max(a))
print(sum(a))
print(sum(a)//len(a))#average of list elements
print(sum(a[1::2])/len(a[1::2]))#average ofall alternate elements


# In[13]:


sum(a[0::3])#9,2


# In[14]:


len(a[0::3])#


# In[15]:


#methode of list
a=[1,9,6,18,2]
a.append(24)#adding a new element at end of list
a
a.insert(2,56)#adding element at particular index
a
a.count(18)#return the value how many times the object repeated
#a.index(56)
#a.sort()#sorts the list in ascending order
a
#a.pop()#removes the last item from the lista=[1,9,6,18,2]
a
#a.pop(1)#remove the element from a particular index
b=[123,23,45] 
#a.extend(b)#merge list 2 into list1
a


# In[16]:


a=[1,9,6,18,2]
a.append(24)#adding a new element at end of list
a
a.insert(2,56)#adding element at particular index
a
a.count(18)#return the value how many times the object repeated
a.index(56)
a.sort()#sorts the list in ascending order
a
a.pop()#removes the last item from the list
a
#a.pop(1)#remove the element from a particular index
#b=[123,23,45] 
#a.extend(b)#merge list 2 into list1
a


# In[17]:


a=[1,9,6,18,2]
a.append(24)#adding a new element at end of list
a
a.insert(2,56)#adding element at particular index
a
a.count(18)#return the value how many times the object repeated
a.index(56)
a.sort()#sorts the list in ascending order
a
a.pop()#removes the last item from the list
a
a.pop(1)#remove the element from a particular index
b=[123,23,45] 
#a.extend(b)#merge list 2 into list1
a


# In[18]:


a=[1,9,6,18,2]
a.append(24)#adding a new element at end of list
a
a.insert(2,56)#adding element at particular index
a
a.count(18)#return the value how many times the object repeated
a.index(56)
a.sort()#sorts the list in ascending order
a
a.pop()#removes the last item from the list
a
a.pop(1)#remove the element from a particular index
b=[123,23,45] 
a.extend(b)#merge list 2 into list1
a


# In[19]:


#function to find second large item from the list
#input:[1,19,6,2,8,,3]
#output:18
def secondlarge(a):
    a.sort()
    return a[-2]

#to find nth largest element
def genericLarge(a,n):
    a.sort()
    return a[-n]
a=[1,19,6,2,8,18,3]
genericLarge(a,4)


# In[20]:


#function to find second least elment
def  secondLeast(a):
    a.sort()
    return a[1]
a=[1,19,6,2,8,18,3]
secondLeast(a)


# In[21]:


#function to find second least elment
def  secondLeast(a):
    a.sort()
    return a[1]
def genericLeast(a,n):
    a.sort()
    return a[n-1]
a=[1,19,6,2,8,18,3]
genericLeast(a,4)


# In[22]:


#function to search data in list
#search is  found then return thte index if not -1
def linearSearch(a,taritem):
    for x in range (len(a)):
        if a [x] == taritem:
            return x
    return -1
a=[1,19,6,2,8,18,3]
linearSearch(a,225)
linearSearch(a,18)


# In[23]:


#function  to search element and print its all index numbers
#input:[1,5,9,6,5,15,1,2,5],key=5,#duplicate
#output:1 4 8 
def linearSearch2(a,taritem):
    for x in range (len(a)):
        if a[x] == taritem :
            print(x,end=" ")
    return 
a=[1,5,9,6,5,15,1,2,5]
linearSearch2(a,5)


# In[24]:


#function
#input:list
#output:seq of characters
#testcase
#[1,5,9,6,5,15,1,2,5],tra=5---!! !!!!! !!!!!!!!!
def linearSearch3(a,taritem):
    for x in range (len(a)):
        if a[x] == taritem :
            j=0
            while j!=x+1:
                print(" !",end="")
                j=j+1
            print(end="   ")
            
    return 
a=[1,5,9,6,5,15,1,2,5]
linearSearch3(a,5)


# In[25]:


#function
#input:list
#output:format
#testcase:
#[12,2,45,9,18,15,36]-------60
# A list item which is perfectly multiple 3 and 5-----45+15=60
def  linearSearch4(a):
    sum=0
    for x in range (len(a)):
        if a[x]%3==0 and a[x]%5==0 :
            sum=sum+a[x]
    return sum
a=[12,2,45,9,18,15,36]
linearSearch4(a)

    


# In[26]:


#function
#input:list
#output:formated output
#testcase:
#=[1,3,8,15,5]#print first and last as it is because first deosnt have previous num and last doesnt have next num
#[6,5,2,8,2]=[6,12,40,4,2]
def linearSearch5(a):
    for x in range (len(a)):
        if x==0 or x==len(a)-1 :
            print(a[x],end=" ")
        else :
            print(a[x-1]*a[x+1],end=" ")
    return
a=[1,2,3,4,5]
linearSearch5(a)


# In[27]:


#function
#input:list
#output:formated output
#testcase:
#[1,6,9,4,16,19,22]---1 9 19 22
#print first and last numbers as it is....and print numbers which has both sides even numbers
def linearSearch6(a):
    for x in range (len(a)):
        if x==0 or x==len(a)-1 :
            print(a[x],end=" ")
        elif a[x-1]%2==0 and a[x+1]%2==0 :
            print(a[x],end=" ")
    return
a=[1,6,9,4,16,19,22]
linearSearch6(a)


# ###number to list
# .input as number
# .expected output is list

# In[28]:


#function for conversation
#input ---number
#output---list
#testcases:-
#14569---[1,4,5,6,9]
#1990----[1,9,9,0]
a=[1,4,5,6,9]
def numberListConversation(n):
    a=[]
    while n!=0 :
        r=n%10
        a.append(r)
        n=n//10
    a.reverse()
    return a
numberListConversation(14569)


# In[29]:


#function to count the occurances of a character in a string
# "python programmimg" , p->2
# "python programmimg" , m->2
def countCharOccurances(s,c):
    cnt=0
    for ch in s:
        if ch==c:
            cnt+=1
    return cnt
countCharOccurances("Python Programming",'m')


# In[30]:


#function to count the occurances of a character in a string
# "python programmimg" , p->2
# "python programmimg" , m->2
def countCharOccurances(s,c):
    cnt=0
    for ch in s:
        if ch==c:
            cnt+=1
    return cnt
def countCharOccurances1(s,c):
    return s.count(c)
countCharOccurances1("Python Programming",'m')

# string to list conversion
:input will be a string
:expected output will be a list

# In[31]:


#function to convert string to list
#testcase
#"1 2 3 4 5 6"--[1,2,3,4,5,6]
def stringToListConversion(s):
    a=s.split()
    numberslist=[]
    for i in a:
        numberslist.append(int(i))
    return numberslist
s="1 2 3 4 5 6"
stringToListConversion(s) 


# SORTING ALGORITHMS:
# all sorting algorithms arrange them in ascending order
# .bubble sort
# .selection sort
# .insertion sort
#    #bubble sort:
#                this algorithm compare the adjacent elements,if the first element is greater
#                 than second element then its required to swap the elements
#  

# In[32]:


#function to represent bubblesort algorithm
def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[19,1,25,6,18,3]
bubbleSort(a)


# In[33]:


li="hyd"
print(li*5)


# In[34]:


if(x%2==0):
    print("even")
else:
    print("odd")
#drivercode
evenodd(6)
evenodd(9)


# In[35]:


def myFun(x):
    
    x=[20,30,40]
lst=[10,11,12,1,3,14,1,5]
myFun(lst)
print(lst)


# ###tuples
# -t1 parenthesis() li square brackets[]
# -difference between list and tuples
#          --list are mutable-can be changed\modified  
#             -used to acces add,modify,delete data
#          -tuples  are immutable-cannot be changed
#              -used to access  data only
#             

# In[36]:


t1=(1,2,3,4,5,6)
type(t1)


# data structures
#    dictionaries
# ###dictionaries
# it works on a concept of set unique data
# keys,values
# is the unique identifier of a object
# each key is separted from its values with colon(:)
# each key and value is separated by comma(,)
# dictionaries enclosed with curly brackets(})
# 

# In[37]:


d1={"name":"gitam","emailid":"gitam@gmail.com","address":"hyderabad"}
print(d1)


# In[38]:


d1["name"]#access the specific key value 


# In[39]:


d1["emailid"]="gitam-python2gmail.com"#update the value


# In[40]:


d1["emailid"]


# In[41]:


del d1["emailid"]#del particular key value 


# In[42]:


print(d1)


# In[43]:


d1.keys()#returns the list of keys


# In[44]:


d1.values()#returns the list of values


# In[45]:


d1.items()#the list of tuples of keys and values


# In[46]:


###contact application
#add contact
#search the contact
#list ofcontacts
#name1:phone1
#name2:phone2
#modify the contact
#remove the contact
#import the contact


# In[47]:


#add contact
contacts={}#creating a dict object
def addContact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contact details are added")
    else:
        print("contact details already exists")
    return
addContact("sruthi","6309082969")
addContact("sai","6309082969")
addContact("sruthi","6309082969")


# In[48]:


#search for contact details
def searchContact(name):
    if name in contacts:
        print(name, ":",contacts[name])
    else:
        print("%s doesnt exist" %name)
    return
searchContact("sruthi")
searchContact("sai")
searchContact("saisruthi")


# In[49]:


#merge contact with existing one
def importContact(newcontacts):
    contacts.update(newcontacts)
    print(len(newContacts.keys()),"contacts added successfully")
    return
newContacts={'msv':27548756069,'nr':48729576}
importContact(newContacts)


# In[10]:


contacts


# In[11]:


#delete a contact
def deleteContact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted successfully")
    else :
        print(name,"not exists")
    return
deleteContact("sai")
deleteContact("knr")


# In[12]:


contacts


# In[6]:


#update contactb details
def deleteContact(name,phone):
    if name in contact:
        contacts[name]=phone
        print(name,"updated successfully")
    else:
        print(name,"not exists")
    return
deleteContact("sruthi",6301458488)
deleteContact("sai",6309082969)


# In[4]:


#assignment
#function to generate series
def generateSeries(n):
    i=0
    for i in range(7):
        x=n**i
        print(x)
        i=i+1
    return
generateSeries(3)


# In[50]:


#assignment
#function to generate series
def generateSeries2(n):
    i=0
    for i in range(10):
        x=n**i
        print(x)
        i=i+1
    return
generateSeries2(2)


# In[79]:


#assignment
#function to generate series
def generateSeries3(a,b,c):
    a=1
    b=3
    c=4                                 
    print(a)
    print(b)
    for sum in range(10):
        sum=a+b+c
        a=b
        b=c
        c=sum
        print(sum)
    return
generateSeries3(1,3,4)


# In[73]:


print type(type(int))


# In[74]:


i=['gitam','college','university']
i.count(1)


# In[75]:


list1=[1,2,3,4,5,6]
list2=[1,2]
print(list(set(list1)-set(list2)))


# In[76]:


type(type(int))


# In[78]:


#assignment
#function for febannaci series
def reverseFibonacci(n): 
   a = [0] * n  
   a[0] = 0 
   a[1] = 1
   for i in range(2, n):   
       a[i] = a[i - 2] + a[i - 1]  
   for i in range(n - 1, -1 , -1):   
       print(a[i],end=" ")  
n = 10
reverseFibonacci(n)


# In[84]:


#classical version
li=["python","programming"]
print("%s %s" % (li[0],li[1]))


# In[86]:


print("{0} {1}".format(li[0],li[1]))


# In[93]:


li1=[1,2,3,4]
print("%d %d %d %d" % (li1[0],li1[1],li1[2],li1[3]))


# In[91]:


print("{0} {1} {2} {3}".format(li1[0],li1[1],li1[2],li1[3]))


# ##boolean function true or false
# --islower():true if the string is lowercase/false if the string not in lower case
# --isupper():true if the string is uppercase/false if the string not in upper case
# --istitle():true if string contains uppercase characters
# --isalpha():true if string contains only alphabets/false
# --isnumeeric():true if string contains numbers/false
# --isspace():true if string contains spaces/false

# In[92]:


s1="gitam"
print(s1.upper())
print(s1.lower())


# In[95]:


s2="Python Programming"
s3="python Programming"
print(s2.istitle())
print(s3.istitle())


# In[98]:


s2="Application1889"
s3="PythonProgramming"
print(s2.isalpha())
print(s3.isalpha())


# In[99]:


s1="1234"
s2="Application123"
print(s1.isnumeric())
print(s2.isnumeric())


# In[100]:


s1=" "
s2="py th on"
print(s1.isspace())
print(s2.isspace())

STRING METHODS
1.join()----method will concatinate two strings
2.split()---split() returns the list of strings separated by whitespace(no parameters are given)
3.replace()---replaces the specific word with given word
# In[102]:


s1="python"
print("".join(s1))


# In[105]:


s2="python programming easy to learn"
print(",".join(s2))


# In[107]:


li=['python','programming','learn']
print(",".join(li))


# In[109]:


s2="python programming easy to learn"
print(s2.split())


# In[111]:


s2="python programming easy to learn"
print(s2.split('a))


# In[114]:


s2="python programming easy to learn"
li=s2.split()
print(li)
print(len(li))


# In[115]:


s2="python programming easy to learn"
li=list(s2)
print(li)


# In[116]:


s2="python programming easy to learn"
print(s2.replace("gra","application"))


# In[1]:


items=[2,4,56,7]
print("list of items" ,items)


# pacakges and modules
# packages:
# -a colection of modules(single python file.py) and subpackages
# module:
# -a single python file containing set of functions
# packages-->subpackages--->modules-->functions-->

# In[2]:


#import external packages of external files
import math
math.floor(123.45)


# In[3]:


from math import factorial as fact
fact(5)


# In[39]:


#assignment
def generateSeries4(n):
    a=2
    i=0
    print(a)
    sum=2
    for i in  range(1,10) :
        x=sum+n*i
        sum=x
        i=i+1
        print(x)
    return
generateSeries4(13)
        


# In[52]:


#assignment
def generateSeries5(n):
    a=8
    b=1
    c=n//2
    print(1)
    for i in range(1,c+1):
        for i in range(1,3):
            b=b+a
            print(b)
            a=a+8
    return
generateSeries5(10)


# In[ ]:


#assignment


# In[7]:


#function to generate n randon numbers in given range
import random
def randomNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
randomNumbers(10,0,100)


# In[36]:


#create a simple game
#generaet 20 random numbers 0 to 500
#input:number
#output:congrats!!
#         try once again!!
import random
def randomNumbers1(n,lb,ub):
    li = [1,2,3,3,4,56,7,6]
    for i in range(0,n):
        li.append(random.randint(lb,ub)) 
    return li
def check(n):
    if n in li:
        return "congrats!!!"
    else :
        return "try once again!!!"
    return
check(15)


# In[ ]:





# In[ ]:




