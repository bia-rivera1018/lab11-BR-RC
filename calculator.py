# https://github.com/bia-rivera1018/lab11-BR-RC.git
# Partner 1: Bianca Rivera
# Partner 2: Rodrigo Cardenas

import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a,b):
    if a<-0 or a==1 or b<=0:
        raise ValueError("Invalid arguments for logarithm.")
    return math.log(b,a)

def exp(a,b):
    return a ** b

def square_root(a):
    if a<0:
        raise ValueError("Cannot take the square root of negative number.")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)