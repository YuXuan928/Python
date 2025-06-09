import os
import numpy as np

def ShowData(ary):
    #顯示資料
    r=ary.shape[0]
    c=ary.shape[1]
    print("  學號  國文  數學   英文  總分  平均")
    for i in range(0, r): 
        #rsum=0
        for j in range(0,c):
            #if(j>0 and j<4):
            #    rsum+=ary[i][j]
            ary[i][4]=sum(ary[i,1:4])     #rsum
            if j==0:
                print(f'{ary[i][j]:5.0f}', end="")
            elif j==4:
                print(f'{ary[i][j]:6.0f}', end="")
            elif j==5:
                ary[i][j]=ary[i][j-1]/3     #rsum/3
                print(f'{ary[i][j]:6.1f}', end="")
            else:
                print(f'{ary[i][j]:6.0f}', end="")
        print()
    print("       ----  ----  ----  ----  ----")
    result = ary.mean(axis=0)   #columns 平均
    print('     ',end="")    #接下方學號位置(學號不累計-資料空白)
    for j in range(1,6):    #顯示各個科的平均
        print(f' {result[j]:5.1f}', end='')     #由國文...平均

#main
fpath='ch14_numpy\\scores.csv' #本案例使用 score.csv
print(f'路徑={fpath}')
a = np.genfromtxt(fpath, delimiter=',', skip_header=1, encoding='utf-8')   #, encoding="utf-8")
#print(a)
na=np.array(a)
ze=np.zeros((30,2))
print(f'na.shape={na.shape}')
print(f'ze.shape={ze.shape}')
ary=np.hstack([na,ze])  #水平串接
print(f'np.hstack([na,ze])={ary.shape}')
ShowData(ary)   #統計並顯示資料


