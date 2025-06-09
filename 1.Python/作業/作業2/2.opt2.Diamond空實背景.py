# -*- coding: utf-8 -*-
#本案例可以選擇有無背景、有無邊框且邊框數選擇
#'菱形-無背景'
def diamond1(n, m):        #方法 無背景
    s, t, str = '★', '　', ''    #多重指派
    tt =  "★" if(m == 0) else "　";     #m>0為有邊框
    x=1
    for i in range(1,2*n):
        for j in range(1,2*n):            
            k = int((2 * n - x) / 2 + 1)    #每列開始有實心星星的位置
            if m==0:
                str = str + s if (j >= k and j < (k + x)) else str + t  #菱形部份實心，其餘兩邊空白星
            else:
                str = str + s if (j >= k and j < (k + x) and (j < (k + m) or j > (2 * n - k - m))) else str + tt #有邊框m
        str+="\n"
        x=x+2 if i<n else x-2
    return str
#-------------

#'菱形-有背景'
def diamond2(n, m):        #方法 有背景
    s, t, str = '★', '☆', ''    #多重指派 #對比方法1 由t='　'改t='☆'
    tt =  "★" if(m == 0) else "☆";     #m>0為有邊框；#對比方法1 由else tt='　'改else tt='☆'
    x=1
    for i in range(1,2*n):
        for j in range(1,2*n):            
            k = int((2 * n - x) / 2 + 1)    #每列開始有實心星星的位置
            if m==0:
                str = str + s if (j >= k and j < (k + x)) else str + t  #菱形部份實心，其餘兩邊空白星
            else:
                str = str + s if (j >= k and j < (k + x) and (j < (k + m) or j > (2 * n - k - m))) else str + tt #有邊框m
        str+="\n"
        x=x+2 if i<n else x-2
    return str
#-------------
        
#main 主程式
n=6
while (n>2):
    n = int(input("請輸入 大於2且小於13 的正整數[每邊的星星數]：<0:結束>"))
    if n==0:
        continue
    n=3 if(n<3) else n
    n=12 if(n>12) else n
    bg=0
    while bg>=0 :
        bg= int(input("請選擇 0)無背景；  1)有背景  -1)結束 :")) #background selected
        if bg==-1:
            break
        side=2
        while  side>0:
            side= int(input("請選擇邊框數[應小於邊長星星數] <0:為無邊框[實心]； -1:結束> :")) #
            if side==-1:
                break
            elif side>n:
                print(f'邊框數{side}應該小於邊長的星星數{n}!')
                continue
                
            if bg==0 :
                print('#菱形-無背景, 邊框：'+str(side))
                print(diamond1(n,side))     #:每邊星星數；side:每邊的邊框數
            elif bg==1:        
                print('#菱形-有背景, 邊框：'+str(side))
                print(diamond2(n,side))
        bg = -1 if side==-1 else side   #bg=-1退出 while bg>=0 [第2個while]
    n = -1 if bg == -1 else n  # 如果要直接退出 while (n>2): [第1個while] 
            
