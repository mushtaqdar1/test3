Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a+=100
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a+=100
NameError: name 'a' is not defined
>>> a=+100
>>> b=+200
>>> print (a)
100
>>> print (b)
200
>>> a=int(input("Enter the first value"))
Enter the first value12
>>> b=int(input("enter the 2nd value"))
enter the 2nd value30
>>> print("the sum of ist and 2nd valus:", a+b)
the sum of ist and 2nd valus: 42
>>> print("the difference of ist and 2nd valus:", b-a)
the difference of ist and 2nd valus: 18
>>> print("the div of ist and 2nd valus:", a/b)
the div of ist and 2nd valus: 0.4
>>> the div of ist and 2nd valus: 0.4
SyntaxError: invalid decimal literal
>>> print("the cube of ist and 2nd valus:", a**3)
the cube of ist and 2nd valus: 1728
