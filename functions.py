# -*- coding: utf-8 -*-
"""Functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pd4Bj9Z4-vFHukwYmgPOOrOHzdBY0NOG
"""

print(dir(str))

a='hello world'
b=a.upper()
print(b)

a='Hello World'
b=a.lower()
print(b)

a='Hello World'
b=a.title()
print(b)

a='Hello World'
b=a.swapcase()
print(b)

a='Hello World'
b=a.replace('Hello','Hii')
print(b)

a='12234'
b=a.isdigit()
print(b)

a='122MY34'
b=a.isdigit()
print(b)

a=range(10)
b=list(a)
print(b)

my_list=list(range(5,15,2))
print(my_list)

def add_numbers(a,b):
    result=a+b
    return result
print(add_numbers(67,89))

def greet(name, greeting="Hello"):
  print(f"{greeting}, {name}!")
greet("Alice")

def calculate_sum(*args):
  total = sum(args)
  return total
print("sum of 1,2,3,4:", calculate_sum(1,2,3,4))
print("sum of 10,20,30:", calculate_sum(10,20,30))

correct_username='admin'
correct_password='1234'
while True:
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username == correct_username and password == correct_password:
    print("Login successful!")
    break
  else:
    print("Invalid username or password. Please try again.")

print(dir(int))

a='Hello World'
b=a.casefold()
print(b)

a='Hello World'
b=a.find('W')
print(b)

def result(n):
  if n>=40:
    return 'pass'
  else:
      return 'fail'
result(50)