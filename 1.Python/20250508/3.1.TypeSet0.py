# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:07:56 2024

@author: Felix
"""

def PadLeft(str, num, padstr):
    stringlength = len(str)
    n = num - stringlength
    if n >= 0:
        str = padstr*n + str
    return str




print('1. 垂直遞增, 正立, 數字' )
n=5
s1=s2=s3=st=''
for i in range(1,n+1):
    #print(s*i, end="")         #同 print(PadLeft('', i-1, '  '), end="")
    s1+=""*(n-i)
    s2+=" "*(n-i)
    s3+="  "*(n-i)
    for j in range(1,i+1):
        s1 += str(i) + " "   #print(j,end=" ")
        s2 += str(i) + " "   
        s3 += str(i) + " "
    s1+="\n"
    s2+="\n"
    s3+="\n"

st=s1+s2+s3
print(st)



print('2. 水平遞增, 正立, 數字' )
n=5
s1=s2=s3=st=''
for i in range(1,n+1):
    #print(s*i, end="")         #同 print(PadLeft('', i-1, '  '), end="")
    s1+=""*(n-i)
    s2+=" "*(n-i)
    s3+="  "*(n-i)
    for j in range(1,i+1):
        s1 += str(j) + " "   #print(j,end=" ")
        s2 += str(j) + " "   
        s3 += str(j) + " "
    s1+="\n"
    s2+="\n"
    s3+="\n"

st=s1+s2+s3
print(st)





