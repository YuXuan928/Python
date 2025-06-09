# -*- coding: utf-8 -*-
#'菱形-無背景'
def diamond1(n):        #方法 無背景
    s, t, str = '★', '　', ''    #多重指派
    x=1
    for i in range(1,2*n):
        for j in range(1,2*n):            
            k = int((2 * n - x) / 2 + 1)    #每列開始有實心星星的位置
            str = str + s if (j >= k and j < (k + x)) else str + t  #菱形部份實心，其餘兩邊空白星
        str+="\n"
        x=x+2 if i<n else x-2
    return str

#'菱形-有背景'
def diamond2(n):        #方法 有背景
    s, t, str = '★', '☆', ''    #多重指派
    x=1
    for i in range(1,2*n):
        for j in range(1,2*n):            
            k = int((2 * n - x) / 2 + 1)    #每列開始有實心星星的位置
            str = str + s if (j >= k and j < (k + x)) else str + t  #菱形部份實心，其餘兩邊空白星
        str+="\n"
        x=x+2 if i<n else x-2
    return str

        
#main 主程式
n=6
while (n>2):
    n = int(input("請輸入 大於2且小於13 的正整數：<0:結束>"))
    if n==0:
        continue
    n=3 if(n<3) else n
    n=12 if(n>12) else n
    bg=0
    while bg>=0 :
        bg= int(input("請選擇 0)無背景；  1)有背景  -1)結束 :")) #background selected
        if bg==-1:
            break
        elif bg==0:
            print('#菱形-無背景')
            print(diamond1(n))
        elif bg==1:        
            print('#菱形-有背景')
            print(diamond2(n))
  
        

