#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle
print(Rectangle.__doc__)
print(__import__('0-rectangle').__doc__)
my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
print(my_rectangle.__doc__)
