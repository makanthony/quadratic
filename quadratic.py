# -*- coding: utf-8 -*-
"""
Nov 30 2022

Anthony Mak
"""
import math

def plus (a, b, c):
    ans = -b + math.sqrt(math.pow(b, 2) - 4*a*c)/2*a
    return ans

def minus (a, b, c):
    ans = -b - math.sqrt(math.pow(b, 2) - 4*a*c)/2*a
    return ans

def complexCheck (a, b, c):
    ans = math.pow(b, 2) - 4*a*c
    return ans

a, b, c = [int(a) for a in input("With equation in form ax^2+bx+c, enter the values for a, b, and c: ").split()]

complex = complexCheck(a, b, c)

if complex >= 0:
    numPlus = plus(a, b, c)
    numMinus = minus(a, b, c)
    print ('Answer using +b is: ', numPlus, '\nAnswer using -b is: ', numMinus)
    
else:
    print('Error: cannot get square root of a negative number')