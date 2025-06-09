0
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:27:53 2024

@author: Felix
"""
from IPython import get_ipython  #清除畫面用get_ipython().magic('clear')
import math



def topic1(n):
    sum=0
    st='1+'
    for i in range(1, n+1):
        sum+=1/i
        if 1<i<5:
            st+=f'1/{i}+'  
    st+=f'...+1/{n}='     #st=st[:-1] #字串去尾字元
    return sum, st

def topic2(n):
    sum=0
    st='1-'
    for i in range(1, n+1):
        #sum+=2*i-1
        sum += math.pow(-1, i-1)*1/i
        op='+' if i%2==0 else '-'
        if 1<i<5:
            st+=f'1/{i}{op}'  
    st+=f'...-1/{n}='     #st=st[:-1] #字串去尾字元
    return sum, st

def topic3(n):
    sum=0
    st='1+'
    for i in range(1, n+1):
        sum1=1
        for j in range(1, i+1):
            sum1=sum1*j
        sum+=sum1
        if 1<i<5:
            st+=f'{i}!+' 
    st+=f'...+{n}!='           
    return sum, st

def topic4(n):
    sum=0
    st='1+'
    for i in range(1, n+1):
        sum1=0
        for j in range(1,i+1):
            sum1+=1/j
        sum+=sum1
        if 1<i<5:
            st=st+'(1+'
            for k in range(2, j+1):
                st+=f'1/{k}+' 
            st=st[:-1] #字串去尾字元
            st+=')+'
    #print(f'st={st}')   #st=1+(1+1/2)+(1+1/2+1/3)+(1+1/2+1/3+1/4)+
    s=st[-16:-2]    #(1+1/2+1/3+1/4)+
    #print(f's={s}') #s=(1+1/2+1/3+1/4
    st+='...+'+s+f'...+1/{n})='
        
    #st+=f'...+(1+1/2+1/3+...+1/{n})='    
    return sum, st

def topic5(n):
    sum=1
    st='1+'
    for i in range(2, n+1):
        sum += (i-1)/i
        if 1<i<5:
            st+=f'{i-1}/{i}+'  
    st+=f'...{n-1}/{n}='    
    return sum, st

#-------------
def recursion0(n):
    # ans = 1;
    # if (n > 0):
    #     ans = n * recursion0(n - 1)
    ans = 1 if n==1 else n * recursion0(n - 1)
    return ans


def recursion1(n):
    # ans = 0;
    # if (n > 0):
    #     ans = 1/n + recursion1(n - 1)
    ans = 1 if n==1 else 1/n + recursion1(n - 1)    
    return ans

def recursion2(n):
    # ans = 0;
    # if (n > 0):
    #     ans = math.pow(-1, n-1)*1/n + recursion2(n - 1)
    ans = 1 if n==1 else math.pow(-1, n-1)*1/n + recursion2(n - 1)
    return ans

def recursion3(n):
    # ans = 0;
    # if (n > 0):
    #     ans = recursion0(n) + recursion3(n - 1)
    #下式同上段
    ans = 1 if n==1 else recursion0(n) + recursion3(n - 1)
    return ans

def recursion4(n):
    ans = 0;
    if (n > 0):
        ans = recursion1(n) + recursion4(n - 1)
    return ans

def recursion5(n):
    ans = 1 if n==1 else (n-1)/n + recursion5(n - 1)
    return ans

#main()
text= "(1) 1+1/2+1/3+1/4+...+1/10\n"
text+="(2) 1-1/2+1/3-1/4+...-1/10\n"	
text+="(3) 1+2!+3!+4!+...+10!    \n"   
text+="(4) 1+(1+1/2)+(1+1/2+1/3)+(1+1/2+1/3+1/4)+...+(1+1/2+1/3+...+1/10)\n"	
text+="(5) 1+1/2+2/3+3/4...+9/10 \n"	 
text+="※每題皆共10項(n=10); 第1、2、4、5題解答，請顯示到小數以下第7位。\n"

while (True):
    #題目選項
    print(text)
    try :
        x=int(input("請選擇： (1)第1題 (2)第2題 (3)第3題 (4)第4題 (5)第5題  (0)結束 "))
    except ValueError:
        input("請勿輸入非數字的字元!!!...Press any key!")
        continue
    if (x < 0 or x > 5):
        input("請輸入 0-5 之間的數!!!...Press any key!")
        continue;
    elif (x == 0):
        break
    else:
        n=10
        sum = 0
        if (x == 1):     #
            sum,st=topic1(n)
            print(f'迴圈法：{st}{sum:.7f}',end='  ')
            print(f'遞迴法：{recursion1(n):.7f}')
        elif(x == 2):    
            sum,st=topic2(n)
            print(f'迴圈法：{st}{sum:.7f}',end='  ')
            print(f'遞迴法：{recursion2(n):.7f}')
        elif(x == 3):
            sum,st=topic3(n)
            print(f'迴圈法：{st}{sum}',end='  ')
            print(f'遞迴法：{recursion3(n)}')
        elif(x == 4):    
            sum,st=topic4(n)
            print(f'迴圈法：{st}{sum:.7f}')
            print(f'遞迴法：{recursion4(n):.7f}')
        elif(x == 5):
            sum,st=topic5(n)
            print(f'迴圈法：{st}{sum:.7f}',end='  ') #{sum:.0f} 表整數
            print(f'遞迴法：{recursion5(n):.7f}')           
        print()    
        #input("Press any key...")  
        #get_ipython().magic('clear')    #清除畫面
        
        

        