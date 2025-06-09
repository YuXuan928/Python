import os
#import numpy as np
import pandas as pd
import copy

  

def ShowData(df, ispartial):
    #顯示資料
    r=df.shape[0]
    c=df.shape[1]
    fld=df.columns  #取得欄位名稱
    print(f"  {fld[0]}  {fld[1]}  {fld[2]}   {fld[3]}   {fld[4]}  {fld[5]}  {fld[6]}")
    for i in range(0, r): 
        for j in range(0,c):
            if j==0:
                print(f'{df.iloc[i,j]:>5s}', end="")    #:>5s
            elif j==4:
                print(f'{df.iloc[i,j]:6.0f}', end="")
            elif j==5 : #or i==r-1 : #[平均行]與[科平均列]
                print(f'{df.iloc[i,j]:6.1f}', end="")
            else:
                print(f'{df.iloc[i,j]:6.0f}', end="")
         
        print()
    #列印科平均
    if (ispartial==False):  #True:部份資料不顯示科平均
        print("       ----  ----  ----  ----  ----")
        print('     ', end='')
        for j in range(0,len(lst)-1): #名次不作平均
            print(f'{lst[j]:6.1f}', end="")

#main
path=os.getcwd()
#fpath=path+'\\ch14_pandas\\scores.csv'
fpath=path+'\\scores.csv'
print(f'路徑={fpath}')
df0 = pd.read_csv(fpath, encoding='UTF-8') #'ANSI'；encoding='UTF-8' 
##print(f'\n原df0={df0}')
df0['id']=df0['id'].astype(str) #將id數值轉文字
df0.columns = ["學號", "國文", "英文", "數學"]
##print(f'\n改欄名的df0={df0}')
df=copy.deepcopy(df0)   #使用df=copy.deepcopy(df0); df與df0互不影響  
                        #!!如果 df=copy.copy(df0)；df=df0會相互影響
df['總分']=df0.sum(axis=1,numeric_only=True)    #使用 df.sum()會包含平均，改用 df0.sum()   
df['平均']=df0.mean(axis=1,numeric_only=True)   #加第2個參數，否則會有警告
df['名次']=df['總分'].rank(method='min',ascending=False) #method='min' 如SQL的 Rank_over()

lst=list(df.mean(axis=0,numeric_only=True)) #取科平均列成一個list
#GetRankFromDf(df) #計算名次
#df.loc['名次'] = df['總分'].rank(method='min',ascending=False) 



print('#排序前：')
ispartial=False     #True：部份資料不顯示科平均
ShowData(df, ispartial )
#df1=copy.deepcopy(df)   #複製一份

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
    asc= True if ad.upper()=="A" else False
    asc= False if ad.upper()=="D" else True
    ad1= '遞增' if asc==True else '遞減'
    #-----
    df.sort_values(by=slist[sel-1], axis=0, ascending=asc, inplace=True, na_position='last')
    print(f"\n#顯示學生資料：{slist[sel-1]}{ad1}")
    ShowData(df, ispartial) #顯示排序後資料

#先作名次排序
ispartial=True  #True：部份資料不顯示科平均
df.sort_values(by=slist[6], axis=0, ascending=True, inplace=True, na_position='last')
y=5
df1=df.loc[(df['名次']<=y)]
print(f'\n#前{y}名的學生{df1.shape[0]}人')
ShowData(df1,ispartial)

#顯示3科成績都有80分(含)以上的學生
x=80
df1=df.loc[(df['國文']>=x)&(df['英文']>=x)&(df['數學']>=x)]
print(f'\n#三科成績皆>={x}的學生{df1.shape[0]}人')
ShowData(df1,ispartial)




'''
print(f'\ncopyto_df增加總分,平均的df=\n{df}')
print(f'df.iloc[-2,0]={df.iloc[-2,0]}') #末二列第1行 30(學號)
print(f'df.iloc[-1,0]={df.iloc[-1,0]}') #末列第1行(科平均列)的學號欄) 修改成空白(學號)
fcolumn=df.columns
#增設Rows
#df.loc[df.shape[0]+1] =df.mean(axis=0)  #改成不增加科平均列
#dfe=df.iloc[-1]         #取出科平均列(暫不使用)
#df=df.drop(index=df.index[-1],axis=0,inplace=True) #刪除末列(暫不使用)
#df = df.append(dfe, ignore_index=True) #增加末列(暫不使用)
'''