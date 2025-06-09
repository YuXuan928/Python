# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:27:53 2024

@author: Felix
"""
###本題的st前4題採 "+"join
#from IPython import get_ipython  #清除畫面用get_ipython().magic('clear')
import math

def topic1(n):
    sum=0
    lst=[]
    for i in range(1, n+1):
        sum+=i
        lst.append(str(i))
    #st="+".join(lst[:4])+'...+'+lst[-1]+"="
    st="+".join(map(str, lst[:4]))+'...+'+lst[-1]+"=" #同上
    return sum, st

def topic2(n):
    sum=0
    lst=[]
    for i in range(1, n+1):
        sum+=2*i-1
        lst.append(str(2*i-1))
    st="+".join(lst[:4])+'...+'+lst[-1]+"="
    return sum, st

def topic3(n):
    sum=0
    lst=[]
    for i in range(1, n+1):
        sum+=2*i
        lst.append(str(2*i))
    st="+".join(lst[:4])+'...+'+lst[-1]+"="
    return sum, st

def topic4(n):
    sum=0
    lst, ls = [], []
    for i in range(1, n+1):
        sum1=0
        for j in range(1,i+1):
            sum1+=j
            ls.append(str(j))       # ls 純數字項(無'+'號)
        sum+=1/sum1
        s="+".join(ls)              #連ls的各項
        s="1/("+s+")" if i>1 else s #加"1/"及前後小括號 :第1項不需要()
        lst.append(s)               #加入lst，ls即可清除
        ls.clear()
        s=''
    s1=lst[3]   #末項的第4小項
    st="+".join(lst[:4])+'...+'+s1[:-1]+f'...+{n})='
    return sum, st

def topic5(n):
    sum=0
    lst=[]
    for i in range(1, n+1):
        #sum += (-1)**(i-1)*i         #同sum += math.pow(-1, i-1)*i
        sum += math.pow(-1, i-1)*i
        s=f'{i}' if i==1 else f'+{i}' if i%2==1 else f'-{i}' 
        lst.append(s)
    st="".join(lst[:4])+'...'+lst[-1]+"="
  
    return sum, st

#-------------

def recursion1(n):
    ans = 0;
    if (n > 0):
        ans = n + recursion1(n - 1)
    return ans

def recursion2(n):
    ans = 0;
    if (n > 0):
        ans = 2*n-1 + recursion2(n - 1)
    return ans

def recursion3(n):
    ans = 0;
    if (n > 0):
        ans = 2*n + recursion3(n - 1)
    return ans

def recursion4(n):
    ans = 0;
    if (n > 0):
        ans = 1/recursion1(n) + recursion4(n - 1)
    return ans

def recursion5(n):
    ans = 0;
    if (n > 0):
        ans = (-1)**(n-1)*n + recursion5(n - 1)
    return ans

text= "1) 1+2+3+4+...+50  \n"
text+="2) 1+3+5+7+...+99  \n"
text+="3) 2+4+6+8+...+100 \n"
text+="4) 1+1/(1+2)+1/(1+2+3)+1/(1+2+3+4)+...+1/(1+2+3+...+50)\n"
text+="5) 1-2+3-4+...-50  \n"
text+=" ※每題皆共10項(n=50); 第4題顯示到小數7位)\n"
while (True):
    #題目選項
    print(text)
    try :
        x=int(input("請選擇： (1)第1題 (2)第2題 (3)第3題 (4)第4題 (5)第5題  (0)結束 "))
    except ValueError:
        input("請勿輸入非數字的字元!!!...Press any key!")
        continue
    if (x < 0 or x > 5):
        input("請輸入 0-5 之間的數")
        continue;
    elif (x == 0):
        break;
    else:
        n=50
        sum = 0
        if (x == 1):     #
            sum,st=topic1(n)
            print(f'迴圈法：{st}{sum}',end='  ')
            print(f'遞迴法：{recursion1(n)}')
        elif(x == 2):    
            sum,st=topic2(n)
            print(f'迴圈法：{st}{sum}',end='  ')
            print(f'遞迴法：{recursion2(n)}')
        elif(x == 3):
            sum,st=topic3(n)
            print(f'迴圈法：{st}{sum}',end='  ')
            print(f'遞迴法：{recursion3(n)}')
        elif(x == 4):    
            sum,st=topic4(n)
            print(f'迴圈法：{st}{sum:.7f}',end='  ')
            print(f'遞迴法：{recursion4(n):.7f}')
        elif(x == 5):
            sum,st=topic5(n)
            print(f'迴圈法：{st}{sum:.0f}',end='  ') #{sum:.0f} 表整數
            print(f'遞迴法：{recursion5(n)}')           
        print()    
        #input("Press any key to exit.")  
        #get_ipython().magic('clear')    #清除畫面
        
        

        