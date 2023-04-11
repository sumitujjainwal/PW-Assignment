#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().set_next_input('Q1. Who developed Python Programming Language');get_ipython().run_line_magic('pinfo', 'Language')
Ans. Guido van Rossum developed Python Programming Language.

get_ipython().set_next_input('Q2. Which type of Programming does Python support');get_ipython().run_line_magic('pinfo', 'support')
Ans. Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of their features support functional programming and aspect-oriented programming (including metaprogramming and metaobjects).

get_ipython().set_next_input('Q3. Is Python case sensitive when dealing with identifiers');get_ipython().run_line_magic('pinfo', 'identifiers')
Ans. Yes, Python is a case-sensitive language, i.e., it treats uppercase and lowercase characters differently. This applies to identifiers too. Easebuzz ID: E230201ZKLXPHW---

get_ipython().set_next_input('Q4. What is the correct extension of the Python file');get_ipython().run_line_magic('pinfo', 'file')
Ans. The file extensions for Python are-
1. .pyz
2. .pyd
3. .pyw
4. .pyo
5. .pyc
6. .pyi
7. .py

get_ipython().set_next_input('Q5. Is Python code compiled or interpreted');get_ipython().run_line_magic('pinfo', 'interpreted')
Ans. Python is both compiled as well as an interpreted language, which means when we run a python code, it is first compiled and then interpreted line by line but the compilation part is hidden from the programmer. The compile part gets deleted as soon as the code gets executed in Python so that the programmer doesn’t get onto unnecessary complexity.


get_ipython().set_next_input('Q6. Name a few blocks of code used to define In Python language');get_ipython().run_line_magic('pinfo', 'language')
Ans. In Python, there are several blocks of code that are used to define different structures, including:
1. Functions: Functions are blocks of code that perform a specific task and can be called multiple times in a program. They are defined using the "def" keyword, followed by the function name and the function parameters in parentheses.
2. Classes: Classes are blocks of code that define objects and their behaviors. They are defined using the "class" keyword, followed by the class name and a colon.
3. Loops: Loops are blocks of code that repeat a set of instructions for a specified number of times or until a certain condition is met. There are two main types of loops in Python: "for" loops and "while" loops.
4. Conditional statements: Conditional statements are blocks of code that execute a set of instructions based on a condition. The two main types of conditional statements in Python are "if" statements and "if-else" statements.
5. Try-except blocks: Try-except blocks are blocks of code used to handle exceptions (errors) that may occur during the execution of a program. The "try" block contains the code that may raise an exception, and the "except" block contains the code that will be executed if an exception occurs.


    
get_ipython().set_next_input('Q7. State a character used to give single-line comments in Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans. Hash character (#) is used to give single-line comments in the Python program. Comments does not have to be text to explain the code, it can also be used to prevent Python from executing code.


    
Q8. Mention functions which can help us to find the version of python that we are currently working on?
Ans.The function sys. version can help us to find the version of python that we are currently working on. We need to import sys package in order to use this function.


    
Q9. Python supports the creation of anonymous functions atruntime, using a construct called __________________
Ans. "Lambda"


    
get_ipython().set_next_input('Q10. What does pip stand for python');get_ipython().run_line_magic('pinfo', 'python')
Ans. pip stands for "preferred installer program".

    
get_ipython().set_next_input('Q11. Mention a few built-in functions in Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans. Some built-in functions in Python are -
1. print( ) function.
2. type( ) function.
3. input( ) function.
4. abs( ) function.
5. pow( ) function.
6. dir( ) function.
6. sorted( ) function.
8. max( ) function.


get_ipython().set_next_input('Q12. What is the maximum possible length of an identifier in Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans. An identifier can have a maximum length of 79 characters in Python.


get_ipython().set_next_input('Q13. What are the benefits of using Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans. There are many benefits to using Python, including:
1. Easy to learn and use: Python has a simple and straightforward syntax, making it easy for new programmers to learn and use.
2. High-level programming language: Python provides high-level data structures and supports dynamic typing, making it a good choice for complex applications.
3. Versatile: Python is used in a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, and more.
4. Large community: Python has a large and active community of developers who contribute to the development of the language and provide support to its users.
5. Open-source: Python is an open-source language, which means that it is free to use and modify, and there are many resources available for learning and using it.
6. Cross-platform compatibility: Python can run on many different operating systems, including Windows, MacOS, and Linux, making it a versatile choice for developers.


get_ipython().set_next_input('Q14. How is memory managed in Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans. Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.


get_ipython().set_next_input('Q15. How to install Python on Windows and set path variables');get_ipython().run_line_magic('pinfo', 'variables')
Ans. To install Python on Windows:
1. Go to the official Python website (https://www.python.org/downloads/) and download the latest version of Python for Windows.
2. Run the Python installation file and follow the on-screen instructions. Make sure to select the option to add Python to your PATH environment variable.
To set the PATH environment variable:
1. Right-click on the Windows Start button and select "System" or search for "Environment Variables" in the Windows search bar.
2. Click on "Environment Variables."
3. Under "System Variables," scroll down and find the "Path" variable, then click on "Edit."
4. Click on "New" and add the path to the Python installation.
5. Click "OK" to close all windows and save the changes.
Now you can open a Command Prompt window and run Python from any location on your computer.


get_ipython().set_next_input('Q16. Is indentation required In python');get_ipython().run_line_magic('pinfo', 'python')
Ans. Yes, indentation is required in Python to define code blocks and scope. It is a crucial part of the Python syntax and used to indicate the start and end of blocks of code. The number of spaces used for indentation is up to the programmer, but it is recommended to use 4 spaces per level of indentation for consistency within the Python community.


# In[1]:


Q1. Explain with an example each when to use a for loop and a while loop.

#for loop
#we use for loop when we need to iteration in any array
#example
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

#we use while loop when we need to satisfied a candition and brak when it is satisfied.
print('\nwhile loop:')
i=0
while i < 4:
    print(i)
    i+=1
1
2
3
4
5

while loop:
0
1
2
3

Q2. Write a python program to print the sum and product of the first 10 natural numbers using for
and while loop.

a = 0
b = 1
for i in range(1,11):
    a = a+i
for j in range(1,11):    
    b = b*j
print(a)
print(b)
55
3628800
sm = 0
ftr = 1
i = 10
while i>0:
    sm = sm+i
    ftr = ftr*i
    i-=1
    
print(sm,ftr)
55 3628800

Q2. Why args and kwargs is used in some functions? Create a function each for args and **kwargs to demonstrate their use.

# in *args we can use multiple values in single definde variable 
def new_fun(*my_value):
    for i in my_value:
        print(i)
new_fun('Hello', 'this', 'is', 'my', 'first', 'definde', 'function')

# in **kargs we can use multiple variable values in single definde variable 

def Multivalue(**my_value):
    for i,j in my_value.items():
        print(i,j)
Multivalue(var1 = 'hello', var2 = 123, var3 = 9.45)
Hello
this
is
my
first
definde
function
var1 hello
var2 123
var3 9.45

Q3. Create a python program to compute the electricity bill for a household. The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit. You are required to take the units of electricity consumed in a month from the user as input. Your program must pass this test case: when the unit of electricity consumed by the user in a month is 310, the total electricity bill should be 2250.

def bill_charge(unit):
    if unit <= 100:
        print('this month total bill: ', unit*4.5)
    elif unit <= 200:
        print('this month total bill: ', unit*6)
    elif unit <= 300:
        print('this month total bill: ', unit*10)
    else:
        print('this month total bill: ', unit*20)
bill_unit = int(input('Enter the bill amount: '))
bill_charge(bill_unit)
Enter the bill amount: 310
this month total bill:  6200

Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print that list.

Number_list = []
for i in range(100):
    cube = i**3
    if cube%4==0 or cube%5==0:
        Number_list.append(i)
print(Number_list)

while i<=100:
    cube = i**3
    if cube%4==0 or cube%5==0:
        Number_list.append(i)
    i+=1
print('\n',Number_list)
[0, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 35, 36, 38, 40, 42, 44, 45, 46, 48, 50, 52, 54, 55, 56, 58, 60, 62, 64, 65, 66, 68, 70, 72, 74, 75, 76, 78, 80, 82, 84, 85, 86, 88, 90, 92, 94, 95, 96, 98]

 [0, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 35, 36, 38, 40, 42, 44, 45, 46, 48, 50, 52, 54, 55, 56, 58, 60, 62, 64, 65, 66, 68, 70, 72, 74, 75, 76, 78, 80, 82, 84, 85, 86, 88, 90, 92, 94, 95, 96, 98, 100]

Q5. Write a program to filter count vowels in the below-given string. string = "I want to become a data scientist"

def count_vowels(text):
    vowels = 'aeiou'
    vowels_list = []
    for i in text:
        if i in vowels:
            vowels_list.append(i)
    print(vowels_list)
    print(len(vowels_list))
text = "I want to become a data scientist"
count_vowels(text)
['a', 'o', 'e', 'o', 'e', 'a', 'a', 'a', 'i', 'e', 'i']
11


# In[2]:


a = [10,20,30,40,50]
for i in a:
    print(i)


# In[4]:


i=0
while i < 10:
    print(i)
    i+=1


# In[6]:


a = 0
b = 1
for i in range(1,20):
    a = a+i
for j in range(1,20):    
    b = b*j
print(a)
print(b)


# In[7]:


sm = 0
ftr = 1
i = 10
while i>0:
    sm = sm+i
    ftr = ftr*i
    i-=1
    
print(sm,ftr)
55 3628800


# In[10]:


sm = 0
ftr = 1
i = 20
while i>0:
    sm = sm+i
    ftr = ftr*i
    i-=1
    
print(sm,ftr)


# In[11]:


def bill_charge(unit):
    if unit <= 100:
        print('this month total bill: ', unit*4.5)
    elif unit <= 200:
        print('this month total bill: ', unit*6)
    elif unit <= 300:
        print('this month total bill: ', unit*10)
    else:
        print('this month total bill: ', unit*20)
bill_unit = int(input('Enter the bill amount: '))


# In[12]:


def bill_charge(unit):
    if unit <= 100:
        print('this month total bill: ', unit*4.5)
    elif unit <= 200:
        print('this month total bill: ', unit*6)
    elif unit <= 300:
        print('this month total bill: ', unit*10)
    else:
        print('this month total bill: ', unit*20)
bill_unit = int(input('Enter the bill amount: '))
bill_charge(bill_unit)


# In[ ]:


Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.

#def keyword is use for create function
lst = []
for i in range(26):
    def odd_num(i):
        if i%2!=0:
            lst.append(i)
        return lst
    odd_num(i)
print(lst)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]


Q2. Why args and kwargs is used in some functions? Create a function each for args and **kwargs to demonstrate their use.

# in *args we can use multiple values in single definde variable 
def new_fun(*my_value):
    for i in my_value:
        print(i)
new_fun('Hello', 'this', 'is', 'my', 'first', 'definde', 'function')

# in **kargs we can use multiple variable values in single definde variable 

def Multivalue(**my_value):
    for i,j in my_value.items():
        print(i,j)
Multivalue(var1 = 'hello', var2 = 123, var3 = 9.45)
Hello
this
is
my
first
definde
function
var1 hello
var2 123
var3 9.45
Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

# With the help of iterator we can traverse through all the values. We use iter() to iterator object and the method used for iteration.
l1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
myitr = iter(l1)
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
2
4
6
8
10


Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

#A generator-function is defined like a normal function, but whenever it needs to generate a value, 
#it does so with the yield keyword rather than return. 
#If the body of a def contains yield, the function automatically becomes a generator function. 

def my_gen(x):
    count = 1
    while count < x:
        yield count
        count+=1
a = my_gen(10)
for i in a:
    print(i)
1
2
3
4
5
6
7
8
9


Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

def generate_primes():
    primes = []
    for num in range(2, 1000):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
primes = generate_primes()
for i in range(20):
    print(next(primes))
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71


Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

def fibo_20_num(num):
    a,b = 0,1
    for i in range(num):
        yield a
        a,b = b, a+b
for i in fibo_20_num(20):
    print(i)
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181


Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’. Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

l = ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
a = [i for i in l]
a
['p', 'w', 's', 'k', 'i', 'l', 'l', 's']


Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

User_input = input('Enter number: ')
rvrs = User_input[::-1]
if rvrs == User_input:
    print('{} it is palindrome'.format(User_input))
else:
    print('{} it is not palindrome'.format(User_input))
Enter number: 12321
12321 it is palindrome
Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.

a = []
s = [a.append(i) for i in range(1, 100)]
l = [i for i in a if i%2==0]
l
[2,
 4,
 6,
 8,
 10,
 12,
 14,
 16,
 18,
 20,
 22,
 24,
 26,
 28,
 30,
 32,
 34,
 36,
 38,
 40,
 42,
 44,
 46,
 48,
 50,
 52,
 54,
 56,
 58,
 60,
 62,
 64,
 66,
 68,
 70,
 72,
 74,
 76,
 78,
 80,
 82,
 84,
 86,
 88,
 90,
 92,
 94,
 96,
 98]
 

