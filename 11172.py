# -*- coding: utf-8 -*-
"""
Created on Spyder

@author: theeSledgehammer
"""

testCases = int(input())

for i in range(testCases):
    a, b = map(int, input().split())
    if a == b:
        print("=")
    elif a>b:
        print(">")
    else:
        print("<")
