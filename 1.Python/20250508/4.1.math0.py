
import math

def topic1(n):
    sum=0
    st=''
    for i in range(1, n+1):
        sum+=i
        if i<4:
            st+=f'{i}+'  
    st+=f'...+{n}='     #st=st[:-1] #字串去尾字元
    return sum, st

def topic2(n):
    sum=0
    st=''
    for i in range(1, n+1):
        sum+=2*i-1
        if i<4:
            st+=f'{2*i-1}+'  
    st+=f'...+{2*n-1}='     #st=st[:-1] #字串去尾字元
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
#------------

text="1) 1+2+3+... (共50項)\n"
text+="2) 1+3+5+... (共50項)\n"
while (True):
    #題目選項
    print(text)

    x=int(input("請選擇： (1)第1題  (2)第2題   (0)結束"))

    if (x < 0 or x > 5):
        print("請輸入 0-5 之間的數")
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
        input("Press any key to exit.")  