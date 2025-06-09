import os
import numpy as np

def GetRank():          #取得名次
    list1=[]
    for i in range(0,ary.shape[0]):
        list1.append(ary[i,4])

    list1.sort()                    #list排續(遞增)
    list1.reverse()                 #list排續(遞減)
    for i in range(ary.shape[0]):   #於list(降冪排序)中找原list[i].tot
        x=list1.index(ary[i,4])    #同list.index(totlist0[i])   
        ary[i,6]=x+1               #寫入ary名次    
        

def ShowData(ary):
    #顯示資料
    r=ary.shape[0]      # r=np.size(ary, 0)
    c=ary.shape[1]      # c=np.size(ary, 1)
    print("  學號  國文  英文   數學   總分  平均  名次")

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
a = np.genfromtxt(fpath, delimiter=',', skip_header=1) 
#print(a) #只有學號及3科成績
na=np.array(a)
'''
#ary作法(1)建立2個columns的空陣列,再填入總分、平均，再併入 na
ze=np.zeros((30,3))     #增2個值=0的空行 原np.zeros((30,2))
ary=np.hstack([na,ze])  #水平串接
#計算總分及平均---  
for x in ary:
    x[4]=sum(x[1:4])   
    x[5]=x[4]/3
'''

#ary作法(2)建立np.sum()、np.mean()、np.zeros()，再column_stack(())
b=np.sum(na[:,1:], axis=1)          #總分欄位
c=np.mean(na[:,1:], axis=1)         #平均欄位
c=np.round(c,1)                     #array的四捨五入
d=np.zeros((30,1))                  #名次的空欄位
ary=np.column_stack((na, b, c, d))  #columns stack
print(ary)
    
GetRank()       #取得名次
print(type(ary))
ShowData(ary)   #統計並顯示資料

#排序欄位選擇
#lists.sort(key=lambda lists: lists[1], reverse=True) #原資料變
#sorted1 = sorted(lists, key=lambda x: x[4]) #原資料不變
slist=['學號', '國文', '英文', '數學', '總分', '平均', '名次']   
while True:
    s=input("\n\n選擇排序欄位[學號,國文,英文,數學,總分,平均,名次：1-7], [結束：0] ")
    if s=='':
        continue
    try:
        sel=int(s);
    except ValueError:
        print('請勿輸入非數字!')
        continue
    if sel==0:
        break
    
    if sel>7 or sel<0:
        print('請輸入 1-7 的正整數!')
        continue
    
    ad=input("\nA)升冪   D)降冪 ") 
    rev= False if ad.upper()=="A" else True  #與df排序升降不一樣!!
    rev= True if ad.upper()=="D" else False
    ad1= '遞增' if rev==False else '遞減'
    #-----
    ary1=sorted(ary, key = lambda x : x[sel-1], reverse=rev)   #True:降冪
    ary1=np.array(ary1)     #上式回傳是串列list?需再轉array
    print(f"\n#顯示學生資料：{slist[sel-1]}{ad1}")
    
    ShowData(ary1) #顯示排序後資料





