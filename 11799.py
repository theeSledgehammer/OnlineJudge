# -*- coding: utf-8 -*-
"""
Created on Spyder

@author: theeSledgehammer
"""

testCases = int(input())
cases = 1
for i in range(testCases):
    mostSpeed = 0
    runners = int(input())
    for j in range(runners):
        scaryCreature = int(input())
        if (j==0):
            mostSpeed = scaryCreature
        elif (scaryCreature > mostSpeed):
            mostSpeed = scaryCreature
            
    print("Case " + str(cases) + ": " + str(mostSpeed))
    cases+=1
