# https://github.com/bia-rivera1018/lab11-BR-RC.git
# Partner 1: Bianca Rivera
# Partner 2: Rodrigo Cardenas

import math

def add(a, b): 
    return a+b

def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def logarithm(a,b):
    if a<-0 or a==1 or b<=0:
        raise ValueError("Invalid arguments for logarithm")
    return math.log(b,a)

def exponent(a,b):
    return a**b #this lowekey tells you who wrote which code - really like it

def square_root(a):
    if a<0:
        raise ValueError("Cannot take the square root of negative number")
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(base, value):
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if value <= 0:
        raise ValueError("Value must be positive.")
    return math.log(value, base)

def exp(a, b):
    return a ** b