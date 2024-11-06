Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=int(input("Input a number: "))
Input a number: 1
 num=int(input("Input Number:"))
 if num ==1:
    print("Monday")
elif(num==2):
    print("Tuesday")
elif(num==5):
    print("Friday")
else:
...     print("Invalid option")
...     
SyntaxError: unexpected indent
>>>  num=int(input("Input Number:"))
...  if num ==1:
...     print("Monday")
... elif(num==2):
...     print("Tuesday")
... elif(num==5):
...     print("Friday")
... else:
...     print("Invalid option")
...     
SyntaxError: unexpected indent
>>> num=int(input("Input Number:"))
... 
... if num ==1:
...    print("Monday")
... elif(num==2):
...    print("Tuesday")
... elif(num==5):
...    print("Friday")
... else:
