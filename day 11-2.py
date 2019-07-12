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


# In[ ]:


sum(a[0::3])#9,2


# In[ ]:


len(a[0::3])#


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


#function to find second least elment
def  secondLeast(a):
    a.sort()
    return a[1]
a=[1,19,6,2,8,18,3]
secondLeast(a)


# In[ ]:


#function to find second least elment
def  secondLeast(a):
    a.sort()
    return a[1]
def genericLeast(a,n):
    a.sort()
    return a[n-1]
a=[1,19,6,2,8,18,3]
genericLeast(a,4)


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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

    


# In[ ]:


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


# In[ ]:


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

# In[ ]:


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


# In[ ]:


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


# In[ ]:


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

# In[ ]:


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

# In[ ]:


#function to represent bubblesort algorithm
def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[19,1,25,6,18,3]
bubbleSort(a)


# In[ ]:


li="hyd"
print(li*5)


# In[ ]:


if(x%2==0):
    print("even")
else:
    print("odd")
#drivercode
evenodd(6)
evenodd(9)


# In[ ]:


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

# In[ ]:


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

# In[ ]:


d1={"name":"gitam","emailid":"gitam@gmail.com","address":"hyderabad"}
print(d1)


# In[ ]:


d1["name"]#access the specific key value 


# In[ ]:


d1["emailid"]="gitam-python2gmail.com"#update the value


# In[ ]:


d1["emailid"]


# In[ ]:


del d1["emailid"]#del particular key value 


# In[ ]:


print(d1)


# In[ ]:


d1.keys()#returns the list of keys


# In[ ]:


d1.values()#returns the list of values


# In[ ]:


d1.items()#the list of tuples of keys and values


# In[ ]:


###contact application
#add contact
#search the contact
#list ofcontacts
#name1:phone1
#name2:phone2
#modify the contact
#remove the contact
#import the contact


# In[ ]:


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


# In[ ]:


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


# In[ ]:


#merge contact with existing one
def importContact(newcontacts):
    contacts.update(newcontacts)
    print(len(newContacts.keys()),"contacts added successfully")
    return
newContacts={'msv':27548756069,'nr':48729576}
importContact(newContacts)


# In[ ]:


contacts


# In[ ]:


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


# In[ ]:


contacts


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


print type(type(int))


# In[ ]:


i=['gitam','college','university']
i.count(1)


# In[ ]:


list1=[1,2,3,4,5,6]
list2=[1,2]
print(list(set(list1)-set(list2)))


# In[ ]:


type(type(int))


# In[ ]:


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


# In[ ]:


#classical version
li=["python","programming"]
print("%s %s" % (li[0],li[1]))


# In[ ]:


print("{0} {1}".format(li[0],li[1]))


# In[ ]:


li1=[1,2,3,4]
print("%d %d %d %d" % (li1[0],li1[1],li1[2],li1[3]))


# In[ ]:


print("{0} {1} {2} {3}".format(li1[0],li1[1],li1[2],li1[3]))


# ##boolean function true or false
# --islower():true if the string is lowercase/false if the string not in lower case
# --isupper():true if the string is uppercase/false if the string not in upper case
# --istitle():true if string contains uppercase characters
# --isalpha():true if string contains only alphabets/false
# --isnumeeric():true if string contains numbers/false
# --isspace():true if string contains spaces/false

# In[ ]:


s1="gitam"
print(s1.upper())
print(s1.lower())


# In[ ]:


s2="Python Programming"
s3="python Programming"
print(s2.istitle())
print(s3.istitle())


# In[ ]:


s2="Application1889"
s3="PythonProgramming"
print(s2.isalpha())
print(s3.isalpha())


# In[ ]:


s1="1234"
s2="Application123"
print(s1.isnumeric())
print(s2.isnumeric())


# In[ ]:


s1=" "
s2="py th on"
print(s1.isspace())
print(s2.isspace())

STRING METHODS
1.join()----method will concatinate two strings
2.split()---split() returns the list of strings separated by whitespace(no parameters are given)
3.replace()---replaces the specific word with given word
# In[ ]:


s1="python"
print("".join(s1))


# In[ ]:


s2="python programming easy to learn"
print(",".join(s2))


# In[ ]:


li=['python','programming','learn']
print(",".join(li))


# In[ ]:


s2="python programming easy to learn"
print(s2.split())


# In[ ]:


s2="python programming easy to learn"
print(s2.split('a))


# In[ ]:


s2="python programming easy to learn"
li=s2.split()
print(li)
print(len(li))


# In[ ]:


s2="python programming easy to learn"
li=list(s2)
print(li)


# In[ ]:


s2="python programming easy to learn"
print(s2.replace("gra","application"))


# In[ ]:


items=[2,4,56,7]
print("list of items" ,items)


# pacakges and modules
# packages:
# -a colection of modules(single python file.py) and subpackages
# module:
# -a single python file containing set of functions
# packages-->subpackages--->modules-->functions-->

# In[ ]:


#import external packages of external files
import math
math.floor(123.45)


# In[ ]:


from math import factorial as fact
fact(5)


# In[ ]:


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
        


# In[ ]:


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


# In[ ]:


#function to generate n randon numbers in given range
import random
def randomNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
randomNumbers(10,0,100)


# In[ ]:


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


# ###file handling inpthon
# file-:document containing information resides on the permanenet storage
# different typesoffile:txt,doc,pdf,csv and etc..
# input:keyboard
# output:file
# ###modesof file input:
# 'w' the mode used to file writing
# ---if the file is not present first it creates the file and write  sort to data
# ---if the file is already present then it will rewrite the previous content

# In[ ]:


#function to create a file and write to the file
def createFile(filename):
    f=open(filename,'w')
    for i in range(10):
        f.write('this is %d Line\n' %i)
    print("file is created and data is written")
    return
createFile('file1.txt')


# In[ ]:


ls


# In[ ]:


def createFile(filename):
    f=open(filename,'w')
    f.write('testing...\n')
    print("file is created and data is written")
    return
createFile('file1.txt')


# In[ ]:


def appendData(filename):
    f=open(filename,'a')
    for i in range(10):
         f.write('this is %d Line\n' %i)
    print("file is created successfully and data is written")
    return
appendData('file2.txt')


# In[ ]:


#function to read of the file
def readFileDate(filename):
    f=open(filename,'r')
    if f.mode== 'r' :
        x=f.read()
        print(x)
    f.close()
    return
readFileDate('file2.txt')


# In[ ]:


#function to read of the file
def fileOperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode == 'a':
            f.write('data to the file')
            print('the data is successfully written')
        f.close()
        return
filename=input('enter the filename')
mode=input('enter the mode of the file')
fileOperations(filename,mode)


# In[ ]:


#data analysis
#word count program
def wordCount(filename,word):
    with open(filename,'r') as f:
        if f.mode =='r':
            x=f.read()
            li=x.split()#it splits the string with whitespace
    cnt=li.count(word)
    return cnt
filename=input('enter the file name : ')
word=input('enter the word :')#which word count you need
wordCount(filename,word)


# In[ ]:


def count(filename):
    with open(filename,'r')as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
            return len(li)
filename=input('enter the filename')
count(filename)


# In[ ]:


def file(filename):
    with open(filename,'r')as f:
        if f.mode=='r':
            x=f.read()
            li=x.split("\n")
            return len(li)
filename=input('enter the filename:')
file(filename)


# In[ ]:


def casecount(filename):
    cntupper=0
    cntlower=0
    with open(filename,'r')as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
    for i in li:
        if i.isupper():
            cntupper+=1
        elif i.islower():
            cntlower+=1
    output='upper case ={0},lowercase={1}'.format(cntupper,cntlower)
    return output
filename= input('enter the filename:')
casecount(filename)


# ###regular expressions
# -used to specific pattern matching
# -symbolic notation of pattern
# 

# In[ ]:


def my_func():
    x=10
    print("the value inside function:",x)
x=20
my_func()
print("the value inside function:",x)    


# ###regular expression for characters
# ->[a-z]---any lowercase character
# --[A-Z]----any uppercase character
# ^[a-z]{5}$---it accepts five lower case characters
# 

# In[ ]:


# function to test two digit number matching
import re
def twodigitnumber(n):
    pattern= '^[0-9]{2}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
print(twodigitnumber(12))#true
print(twodigitnumber(123))#false


# In[ ]:


def testusername(s):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testusername('GitamHYD'))
print(testusername('Gitam188'))

###regular expression to match indian mobile number
-10 digits
-(first digit will be [6-9])and remaining 9 digits will be [0-9]
-ex:6309082969
-re[6 9](0 9){9}$
--example:06309082969(re cap ^[0][6 9][0 9](9)(dollar)
example:+916309082969
re ^[+](9)[1][6 9][0 9](9)

# In[ ]:


def phonenumber(phone):
    pattern= '^[6-9][0-9]{9}$|^[0][6-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
phonenumber(9988774455)


# ---regular expression to validate a roll number
# -example :1521A0501
# -example :1521A0109
# -example :1521A0499
# ---regular exprression to validate a password
# .parameters:len min 0f 6 characters and max of 15 characters
# .accept lowercase,uppercase,digits spl char(@,#,!)

# In[ ]:


def rollValidation(rollnum):
    pattern='^[1][5][2][1][A][0][0-9]{3}$'
    pattern=str(pattern)
    if re.match(pattern,rollnum):
        return True
    return False
rollValidation('1521A0345')


# In[ ]:


def passwordValidation(password):
    pattern='^[a-zA-Z0-9@#!]{6,15}$'
    pattern=str(pattern)
    if re.match(pattern,password):
        return True
    return False
passwordValidation('jjsD@KL')
    


# ###emailid validation
# username:-
#     length will be[6-15]
#     no spl characters apartfrom underscore(_)
#     should not begin and end with underscore(_)
#     characters set:all digits and lowercase
# extension:-
#       length will be[2-4]
#       no spl characters
#       character set:lower case character

# In[ ]:


def emailValidation(email):
    pattern='^[0-9a-z][0-9a-z_.]{5,14}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email) :
        return True
    return False
emailValidation('saisruthi2000@gmail.com')


# ###python turtle
# -turtle graphics
# 

# In[ ]:


#step 1:make all the turtle package to be imported
import turtle
#turtle method creates and returns a new object
a1=turtle.Turtle()
#forward()method moves 100 pixels
turtle.forward(250)
#we are done
turtle.done() 


# In[ ]:


#line draw in reverse direct
import turtle as tt
a1=turtle.Turtle()
tt.backward(100)
tt.done()


# In[ ]:


#draw square
import turtle as tt
a1=tt.Turtle()
a1.forward(150)
a1.right(90) 
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90) 
a1.forward(150)
a1.right(90)
tt.done()


# In[ ]:


#draw the left
import turtle as t
a1=t.Turtle()
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
t.done()


# In[ ]:


#loop statement
import tutrtle as t 
aa=t.Turtle()
for i in range(4):
    aa.backward(150)
    aa.left(90)
t.done()


# In[ ]:


#loop statement
import turtle as t 
aa=t.Turtle()
for i in range(4):
    aa.forward(150)
    aa.right(90)
t.done()


# In[ ]:


#star
import turtle as t
a1=t.Turtle()
for i in range(40):
     a1.forward(50)
        a1.right(144)
t.done()


# In[ ]:


##spiraling star
import turtle as t 
a1=t.Turtle()
a1.pencolor('blue')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done()


# In[ ]:


#hexagon with multi color
from turtle import *
colors=['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)


# In[ ]:


#goto function
from turtle import *
goto(50,50)#
goto(-50,50)
goto(100,-50)
goto(-50,-50)


# In[2]:


#setheading(heading)
#will change direction
from turtle import *
colors=['blue','green','yellow','orange','purple','red']
for angle in range(0,360,15):
    pencolor(colors[angle%6])
    setheading(angle)
    forward(100)
    write(str(angle)+'o')    
    backward(100)


# In[1]:


#undo()function will be undo the turtle last action
from turtle import *
pencolor('blue')
for i in range(15):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolor('red')
for i in range(90)


# In[1]:


from turtle import *
pensize(50)
pencolor('blue')
forward(250)
pencolor(0,1.0,0)
forward(250)
pensize(10)
goto(-400,500)


for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red/4.0,green/4.0,blue/4.0)
            forward(10)
    
    


# In[ ]:


#generate a rectangle
import turtle as tt 
a1=tt.Turtle()
a1.forward(150)
a1.right(90) 
a1.forward(50)
a1.right(90)
a1.forward(150)
a1.right(90) 
a1.forward(50)
a1.right(90)
tt.done()


# #generate a rectangle
# #generate a circle
# fill colors in circle and rectangle
# #fillcolor('color')
# #stamp()

# In[2]:


#generate the symbols
from turtle import *
colors=('red','orange','yellow','seagreen4','orchid4','royalblue1')
reset()
up()
goto(-320,-195)
width(90)
for pcolor in colors:
    color(pcolor)
    down()
    forward(750)
    up()
    backward(750)
    left(90)
    forward(100)
    right(90)
width(20)
color('white')
goto(0,-170)
down()

circle(170)
left(90)
forward(340)
up()
left(180)
forward(170)
up()
backward(170)
left(90)
down()
forward(170)
up()
goto(0,300)


# In[3]:


from turtle import *
fillcolor('orange')
pensize(10)
pencolor('black')
forward(100)

begin_fill()
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
end_fill()


# In[1]:


from turtle import *
fillcolor('red')
pensize(10)
pencolor('black')
forward(100)

begin_fill()
circle(150)
end_fill()


# In[2]:


from turtle import *
fillcolor('red')
pensize(25)
pencolor('black')
begin_fill()
circle(250)
end_fill()


# In[ ]:




