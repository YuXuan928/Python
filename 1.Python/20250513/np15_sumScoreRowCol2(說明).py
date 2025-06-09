import numpy as np
import os

def Round_iterator(x,y):    #返回一個調整四捨五入後的array之函式
    c=x.shape[0]            #取得一維陣列x的col值
    b=np.zeros((c,))        #建立一維陣列軸向值col的b陣列
    for i in range(0,c):    #如i改用 _ 表示不在意變量(i or j)的值，只是要執行c圈，可使用i,j替代
        b[i]=round(x[i],y)  
    return b                # 回傳 array b

path=os.path.join(os.getcwd()) 
fpath=os.path.abspath(os.path.join(path, 'ch14_numpy\\scores.csv'))
na = np.genfromtxt(fpath, delimiter=',', skip_header=1)
print(na)
print('國文最高分數：na[:,1].max()=', na[:,1].max())
print('英文最低分數：na[:,2].min()=', na[:,2].min())
print('數學平均分數：na[:,3].mean()=', na[:,3].mean())
total1 = na[:,1] + na[:,2] + na[:,3]
print(f'\n個人總分1={total1}')
print('全班最高總分1：na[:,1] + na[:,2] + na[:,3]=',total1.max())

total2 = na[:,1:4].sum(axis=1)  #三科合計； total2=total1
print(f'\n個人總分2={total2}')
print('全班最高總分2：na[:,1:4].sum(axis=1)=',total2.max())
print()
print(f'國文平均分數：na[:,1:4].sum(axis=1)={na[:,1].mean():5.1f}')
print(f'英文平均分數：na[:,2].mean():6.1f={na[:,2].mean():5.1f}')
print(f'數學平均分數：na[:,3].mean():6.1f={na[:,3].mean():5.1f}')


print(f'國英數各科總分1：sum(na[:,1:4])=        {sum(na[:,1:4])}') 
print(f'國英數各科總分2：na[:,1:4].sum(axis=0)= {na[:,1:4].sum(axis=0)}')
print(f'各column合計  ：sum(na[:,:])=          {sum(na[:,:])}\n')

a=sum(na[:,1:4])/30
print(f'國英數各科平均(未取小數1位)a=：{a}')
b1=np.round(a,1) #取小數1位
print(f'國英數各科平均(取小數1位)b1={b1}')
b2=Round_iterator(a,1) #取小數1位
print(f'國英數各科平均(取小數1位)b2={np.round(b2,1)}\n')




 