"""
Created on lInUx!!!

@author: theeSledgehammer
621 - S e c r e t  R e s e a r c h
"""
loop = int(input())
for i in range(loop):
    num = int(input())
    if num == 1 or num == 4 or num == 78:
        print("+")
    elif str(num).endswith('35'):
        print("-")
    elif str(num).startswith('190'):
        print("?")
    else:
        print("*")
