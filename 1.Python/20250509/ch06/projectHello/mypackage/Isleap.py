# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 23:12:23 2024
@author: Felix
"""

tf, msg = False, ''
def IntTryParse(value):
    try:
        return [str(int(value)), True]  #傳回list
    except ValueError:
        return [value, False]           #傳回list

def MyIsLeap(y):
    list1 = IntTryParse(y)	##check 是否文數字
    if list1[1]==False :
        msg=("傳入值不是數字!")
    else:        
        tf = False
        if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
            tf=True
        msg=f'{y:4d}:是閏年!' if tf==True else f'{y:4d}不是閏年!'    
    return msg
    







