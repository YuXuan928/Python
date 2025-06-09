# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 02:50:32 2024

@author: Felix
"""
def diamond1(n):
    i=1
    str = "";
    #原正立置中
    for i in range(1, n+1):
        for k in range(1, n - i + 1):   #每列加空白("　"個數遞減)，本式並沒有加空白，應可以免，只是作為與下2組(置中、偏右作對比)
            str += t                   #不加空白
        for j in range(1, i+1):         #由左而右顯示(★個數遞增)
            str += s + t                #星號加空白
        str+="\n"
    #原倒立置中range(1,n+1)改成range(2,n+1)
    for i in range(2, n+1):     #range(1,n+1)改成range(2,n+1)
        for k in range(1, i):   #每列加空白("　"個數遞減)，本式並沒有加空白，應可以免，只是作為與下2組(置中、偏右作對比)
            str += t                   #不加空白
        for j in range(1, n-i+2):         #由左而右顯示(★個數遞增)
            str += s + t                #星號加空白
        str+="\n"
    
    return str



def diamond2(n):
    i=1
    str = "";
    for z in range(1,2*n):
        #for k in range(1,n-i+1):
        #    str+=t
        str+='　'*(n-i+1) #本式功能同上k迴圈
            #print(t,end='')
        for j in range(1,i+1):
            str=str+s+t
            #print(s+t,end='')
        str+="\n"
        i=i+1 if(z<n) else i-1
    return str

#---呼叫方法
s='★'
t='　'
str=''
print("#二組迴圈")
print(diamond1(6)+"\n")
print("#一組迴圈")
print(diamond2(6))
         