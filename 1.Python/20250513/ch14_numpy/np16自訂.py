import numpy as np
import math 


def MyPercentile1(a,y):  #自訂百分比值涵數1 y為百分比如0.75
    n=a.shape[0]         #QUARTILE.EXC方法
    mod=n%2
    k=math.floor((n+1)*y)
    if mod==0:
        q1=a[k-1]+(a[k]-a[k-1])*(1-y)
        #42+(43-42)*0.25
    else:
        q1=a[k-1]+(a[k]-a[k-1])*0   #q1=a[k-1]
        #Q3=43+(47-43)*0=43
    #print(f'k={k}、{a[k-1]}、{a[k]}')
    return q1
    

def MyPercentile2(a,y):  #自訂百分比值涵數2 y為百分比如0.75
    n=a.shape[0]         #QUARTILE.INC方法
    mod=n%2
    k=math.floor(1+(n-1)*y)
    if mod==0:
        q2=a[k-1]*(1-y)+a[k]*y
    else:
        q2=a[k-1]*0.5+a[k]*0.5
    #print(f'k={k}、{a[k-1]}、{a[k]}')
    return q2


#a = np.random.randint(100,size=50)
a1=[ 6, 8, 10, 14, 12, 7, 5, 15, 2, 4]     #list 偶數個
#a1=[ 6, 8, 10, 14, 7, 5, 15, 2, 4]        #list 奇數個
a=np.array(a1);             #list 轉 array
a=np.sort(a)
print('陣列的內容：', a)

print('\n#自行計算：')
#-------個人計算
n=a.shape[0]        #軸向數量
#u=np.sum(a)/n       #a的平均數 np.mean(a)
u=np.mean(a)       #a的平均數 
print(f'1.平均數 u={u}')

#變異數
v2=0    
for i in a:
    v2+=math.pow((i-u),2)    #同v2+=pow((i-u),2) 、 v2+=(i-u)**2
v2=v2/n    
#print(f'變異數 v2={v2}')

#標準差
x=math.sqrt(v2)      #同(v2/n)**0.5
print(f'2.標準差 x={x}')

print(f'3.變異數 v2={v2}')

#中位數 奇數取中間，偶數中間2個數的平均

if n/2==int(n/2):
    k=int(n/2)
    m=(a[k-1] + a[k])/2
else:
    m=a[int((n+1)/2-1)]

print(f'4.中位數 m={m}')

#百分比值，有多種不同的方法以及不同的數據 (本例為第三四分位數Q3)
q1=MyPercentile1(a,0.75)
print(f'5.1.自訂百分比值1 Q3：{q1}')
q2=MyPercentile2(a,0.75)
print(f'5.2.自訂百分比值2 Q3：{q2}')

d=np.max(a)-np.min(a)
print(f'6.最大最小差值 d={d}\n')

#-----




