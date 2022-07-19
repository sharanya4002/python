# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:36:33 2022

@author: Sys177
"""

def fib(n):
    a = 2
    b = 1
    if n == 1:
       print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(20)