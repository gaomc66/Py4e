String
----------
>>> str1 = "Hello"
>>> str2 = 'there'
>>> bob = str1 + str2

>>> str3 = '5'
>>> int3 = int(str3)

>>> name = input('enter:')
enter: ***

----------
banana
012345

>>> fruit = "banana"
>>> letter = fruit[1]
>>> print(fruit)
a

>>> x = len(fruit)
>>> print(x)
6

---------
index = 0
while index < len(fruit) :
    x = fruit[index]
    print(index, x)
    index = index + 1

for letter in fruit:
        print(letter)

----------
Looping and Counting

word = "banana"
count = 0
for a in word:
    if count == 'a':
        count ++

------------
Monty Python
01234567891011
>>> s = "Monty Python"
>>> print(s[0:4])
#Range: up tp but not include
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
#No Traceback
Python
>>> print(s[:7])
Monty P
>>> print(s[10:])
on
>>> print(s[:])
Monty Python

-------------
String Concatenation

a = str1 + str2
# no space between to Strings

>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan' in fruit
True
>>> if 'a' in fruit :
    ... ...

--------------
String Comparison
if word  == 'banana'
if word < 'banana'
# A < a
# Z < a
# Chuck < Glenn
# chuck > Glenn

--------------
String Library

>>> greet = 'Hello Bob'
>>> zap = greet.lower()
# make a copy
>>> print(zap)
hello bob
>>> print(great)
Hello bob
>>> print("Hello Bob".lower())
hello bob

>>> stuff = "Hello world"
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
#ducument

>>> pos = fruit.find('na')
>>> print(pos)
2
#first one
>>>  x = fruit.find('x')
-1


---------------
