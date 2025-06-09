import os
import numpy as np


def ShowData(ary):
    #顯示資料
    r=ary.shape[0]      # r=np.size(ary, 0)
    c=ary.shape[1]      # c=np.size(ary, 1)
    print("  學號  國文  英文   數學  總分  平均")
    for i in range(0, r): 
        for j in range(0,c):
            if j==0:
                print(f'{ary[i,j]:5.0f}', end="")
            elif j==4:
                print(f'{ary[i,j]:6.0f}', end="")
            elif j==5:
                ary[i,j]=ary[i,j-1]/3     #rsum/3
                print(f'{ary[i,j]:6.1f}', end="")
            else:
                print(f'{ary[i,j]:6.0f}', end="")
        print()
    print("       ----  ----  ----  ----  ----")
    result = ary.mean(axis=0)   #columns 平均
    print('     ',end="")    #接下方學號位置(學號不累計-資料空白)
    for j in range(1,6):    #顯示各個科的平均
        print(f' {result[j]:5.1f}', end='')     #由國文...平均

#main
path=os.getcwd()
fpath=path+'\\scores.csv'
print(f'路徑={fpath}')
a = np.genfromtxt(fpath, delimiter=',', skip_header=1, encoding="utf-8") 
#print(a) #只有學號及3科成績
na=np.array(a)
ze=np.zeros((30,2))     #增2個值=0的空行 原np.zeros((30,2))
ary=np.hstack([na,ze])  #水平串接
print(f'ary1=\n{ary}')  #只有3科成績

print(na.shape)
print(ze.shape)
print(ary.shape)


#計算總分及平均---  
'''
#方法1
for x in ary:
    x[4]=sum(x[1:4])   
    x[5]=x[4]/3
'''
#方法2
ary[:,4]=ary[:,1:4].sum(axis=1)
ary[:,5]=ary[:,4]/3

#GetRank()       #取得名次
print(type(ary))
ShowData(ary)   #統計並顯示資料

#排序欄位選擇
slist=['學號', '國文', '英文', '數學', '總分', '平均']
while True:
    s=input("\n\n選擇排序欄位[學號,國文,英文,數學,總分,平均：1-6], [結束：0] ")
    if s=='':
        continue
    try:
        sel=int(s);
    except ValueError:
        print('請勿輸入非數字!')
        continue
    if sel==0:
        break
    
    if sel>6 or sel<0:
        print('請輸入 1-7 的正整數!')
        continue
    
    #ad=input("\nA)升冪   D)降冪 ") 
    #asc= False if ad.upper()=="A" else True  #與df排序升降不一樣!!
    #asc= True if ad.upper()=="D" else False
    asc= False if sel==1 else True
    ad1= '遞減' if asc==True else '遞增'
    
    #-----
    ary1=sorted(ary, key = lambda x : x[sel-1], reverse=asc)   #True:降冪
    ary1=np.array(ary1)     #上式回傳是串列list?需再轉array
    print(f"\n#顯示學生資料：{slist[sel-1]}{ad1}") #Column head
    ShowData(ary1) #顯示排序後資料





