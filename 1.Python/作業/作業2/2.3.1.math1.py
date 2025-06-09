# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:27:53 2024

@author: Felix
"""
from IPython import get_ipython  #清除畫面用get_ipython().magic('clear')
import math



def topic1(n):
    sum=0
    st=''
    for i in range(1, n+1):
        sum+=i
        if i<5:
            st+=f'{i}+'  
    st+=f'...+{n}='     #st=st[:-1] #字串去尾字元
    return sum, st

def topic2(n):
    sum=0
    st=''
    for i in range(1, n+1):
        sum+=2*i-1
        if i<5 :
            st+=f'{2*i-1}+'  
    #st+=f'...+{2*n-1}='     #st=st[:-1] #字串去尾字元
    return sum, st

def topic3(n):
    sum=0
    st=''
    for i in range(1, n+1):
        sum+=2*i
        if i<5:
            st+=f'{2*i}+' 
    st+=f'...+{2*n}='           
    return sum, st

def topic4(n):
    sum=0
    st='1+'
    s=''
    for i in range(1, n+1):
        sum1=0
        for j in range(1,i+1):
            sum1+=j
        sum+=1/sum1
        if 1<i<5:
            st=st+'1/(1+'
            for k in range(2, i+1):
                st+=f'{k}+' 
            st=st[:-1] + ')+' #字串去尾字元, 再加')+'
    #print(f'st={st}')  #st="1+1/(1+2)+1/(1+2+3)+1/(1+2+3+4)+"
    s=st[-12:-2]        #s=st[-12:-2]=1/(1+2+3+4
    st+='...+'+s+f'...+{n})='  
    #上式= '1+1/(1+2)+1/(1+2+3)+1/(1+2+3+4)+' +'...' + '1/(1+2+3+4' + '...+50)='
    return sum, st

def topic5(n):                        
    sum=0
    st=''
    for i in range(1, n+1):
        #sum += (-1)**(i-1)*i         #sum += math.pow(-1, i-1)*i
        sum += math.pow(-1, i-1)*i
        op='-' if i%2==1 else '+'
        if i<5:
            st+=f'{i}{op}'    #x += 1 是將變數 x 的原本值加上 1，然後再存回 x 本身，這是一種常見的 「累加」 操作，通常用在：1.計數器2.迴圈內的次數統計3.逐步加總
    last_term = int(math.pow(-1, n-1) * n)  # ex= int(-1 的 (10-1) 次方 * 10) = -10 ➜ st += '...-10=
    st += f'...{last_term}='                 
    return sum, st

#-------------遞迴方法

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
        ans = 1/recursion1(n) + recursion4(n - 1) #用recursion1的原因是:第一的變數就是1加到50逤一直接呼叫recursion1
    return ans

def recursion5(n):
    ans = 0;
    if (n > 0):
        ans = (-1)**(n-1)*n + recursion5(n - 1)  #**是平方的意思(-1)的(n-1)平方乘上n + an 'recursion5(n - 1)'
    return ans

text= "1) 1+2+3+4+...+50  \n"
text+="2) 1+3+5+7+...+50  \n"
text+="3) 2+4+6+8+...+50 \n"
text+="4) 1+1/(1+2)+1/(1+2+3)+1/(1+2+3+4)+...+1/(1+2+3+...+50)\n"
text+="5) 1-2+3-4+...+50  \n"
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
        
        

        