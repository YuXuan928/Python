# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 23:12:23 2024

@author: Felix
"""
#import math
import calendar #islesp()

def IntTryParse(value):
    try:
        return [str(int(value)), True]  #傳回list
    except ValueError:
        return [value, False]           #傳回list

def IsLeap(y):
    tf = False
    if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        tf=True
    return tf 
    


while (True):
    s=input("請輸入西元年份 <結束:0>：")
    list1 = IntTryParse(s)	##check 是否文數字
    if list1[1]==False :
        print("輸入值不是數字!")
        continue
    x=int(s)
    
    if x==0:
        break
    elif x<0:
        continue
    
    tf1=IsLeap(x)
    msg=f'{x:4}:是閏年!' if tf1==True else f'{x:4}不是閏年!'
    print(f'IsLeap：{msg}')
    tf2=calendar.isleap(x)
    msg=f'{x:4}:是閏年!' if tf2==True else f'{x:4}不是閏年!'
    print(f'isleap；{msg}')



