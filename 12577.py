# -*- coding: utf-8 -*-
"""
Created on Spyder

@author: theeSledgehammer
"""

chant = str(input())
case = 0
while (chant != '*'):
    case+=1
    if chant == "Hajj":
        print("Case " + str(case) + ": " + "Hajj-e-Akbar" )
    else:
        print("Case " + str(case) + ": " + "Hajj-e-Asghar" )
    
    chant = str(input())

