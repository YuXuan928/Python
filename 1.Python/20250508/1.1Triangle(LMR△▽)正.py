# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 02:50:32 2024

@author: Felix
"""

#靠左正三角
s = "★";
t = "　";
n = 6;

for i in range(1, n+1):
    str = "";
    for k in range(1, n - i + 1):   #每列加空白("　"個數遞減)，本式並沒有加空白，應可以免，只是作為與下2組(置中、偏右作對比)
        str += ""                   #不加空白
    for j in range(1, i+1):         #由左而右顯示(★個數遞增)
        str += s + t                #星號加空白
    str += "\n"                     #跳(換)下1列
    print(str)          
            

#置中三角形
s = "★";
t = "　";
n = 6;

for i in range(1, n+1):
    str = "";
    for k in range(1, n - i + 1):   #每列加空白("　"個數遞減)，本式並沒有加空白，應可以免，只是作為與下2組(置中、偏右作對比)
        str += t                   #不加空白
    for j in range(1, i+1):         #由左而右顯示(★個數遞增)
        str += s + t                #星號加空白
    str += "\n"                     #跳(換)下1列
    print(str)      
    

#靠右三角形
s = "★";
t = "　";
n = 6;

for i in range(1, n+1):
    str = "";
    for k in range(1, n - i + 1):   #每列加空白("　"個數遞減)，本式並沒有加空白，應可以免，只是作為與下2組(置中、偏右作對比)
        str += t+t                   #不加空白
    for j in range(1, i+1):         #由左而右顯示(★個數遞增)
        str += s + t                #星號加空白
    str += "\n"                     #跳(換)下1列
    print(str)          