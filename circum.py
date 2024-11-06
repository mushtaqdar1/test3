Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> radius=float(input(" Enter the radius of the circle"))
 Enter the radius of the circle 5
>>> area=3.14 * radius**2
>>> print("Area of the circle=",area)
Area of the circle= 78.5
>>> print("circumference of the circle=",circum)area=3.14 * radius**2
SyntaxError: invalid syntax
>>> area=3.14 * radius**2
>>> cicum=2*3.14*radius
>>> print("circumference of the circle=",circum)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("circumference of the circle=",circum)
NameError: name 'circum' is not defined. Did you mean: 'cicum'?
>>> r=int(input("Enter the value of radius="))
Enter the value of radius=2
>>> circum=2*3.14*r
>>> print("circumference=",circum)
circumference= 12.56
