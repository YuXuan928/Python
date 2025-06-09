# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:15:38 2024

@author: Felix
"""
import random

def GetScore(x) :           #回傳單一學生資料
    rng1, rng2 = 40, 100
    tot=k=0
    list1=[]
    list1.append(x)                     #學號加入list
    for i in range(3):
        sco=random.randint(rng1, rng2)  #產生單科成績
        k += 1 if sco<60 else 0         #不及格科目累計
        list1.append(sco)               #逐個科目加入list
        tot+=sco                        #個人總分累計
    avg=tot/3                           #個人平均
    list1.extend([tot, avg, 0, k])      #list同時加多個元素
    return list1                        #回傳list

#----------
def GetRank():          #取得名次
    list1=[]
    for i in range(0,n):
        list1.append(lists[i][4])   
    #因lists=[],需使用lists[i][4]，不能使用lists[i,4]

    list1.sort()                    #totlist排序(遞增)
    list1.reverse()                 #totlist排序(遞減)
    for i in range(n):              #於totallist(降冪排序)中找原list[i].tot
        x=list1.index(lists[i][4])  #同totlist.index(totlist0[i])   
        lists[i][6]=x+1             #寫入名次屬性    
        #print(lists[i][6],end=',')

#----------
def ShowData():
    #顯示資料
    csum=[0]*6  #宣告長度為6的全 0 list
    print("學號  國文  數學   英文  總分  平均  名次  不及格科數")
    for i in range(0, len(lists)):          #r=len(lists)
        for j in range(0,len(lists[1])):    #c=len(lists[1])
            if j==0:
                print(f'{lists[i][j]:3}', end="")   #
            elif j==5:
                print(f'{lists[i][j]:6.1f}', end="")
            elif j==6:
                    print(f'{lists[i][j]:5}', end="")
            elif j==7:
                print(f'{lists[i][j]:7}', end="")
            else:
                print(f'{lists[i][j]:6}', end="")
            if 0<j<6:
                csum[j]+=lists[i][j]
            #因lists=[],需使用lists[i][j]，不能使用lists[i,j]
        print()
    print("     ----  ----  ----  ----  ----")
    
    print('    ',end="")    #接下方學號位置(學號步累計-資料空白)
    for j in range(1,6):
        print(f'{csum[j]/n:5.1f}', end=' ')     #由國文...平均

#----------
#main主程式
n=int(input("請輸入學生人數："))
n=20 if n>20 else n
lists=[]
for i in range(0, n):
    list2=GetScore(i+1)     #學號由1開始 list2為一筆學生資料
    lists.append(list2)     #list2加入二維lists
#print(lists[0])    
#lists.pop(0)                #lists[0]為空資料，先去除
GetRank()                   #取得名次

print('#二維串列的 rows、columns：', end='')
print(f'r={len(lists)}, c={len(lists[1])}')
#print(f"lists[3]={lists[3]}")

ShowData()                  #顯示原資料
print('\n')

#lists.sort(key=lambda lists: lists[1], reverse=True)
#sorted1 = sorted(lists, key=lambda x: x[4]) #原資料不變

#排序欄位選擇
while True:
    sel=int(input("\n\n選擇排序欄位[學號,國文,英文,數學...：1-8], [結束：0]"))
    if sel==0:
        break
    elif sel>8 or sel<0:
        print('請輸入 1-8 的正整數!')
        continue
    
    #list排序
    slist=['學號', '國文', '數學', '英文', '總分', '平均', '名次', '不及格科數']
    if sel==7 or sel==8:
        lists.sort(key=lambda lists: lists[sel-1], reverse=False)   #後二欄遞增排序
    else:
        lists.sort(key=lambda lists: lists[sel-1], reverse=True)    #前6欄遞減排序
    ad= '遞減' if sel<7 else '遞增'
    print(f"\n#顯示學生物件：{slist[sel-1]}{ad}")
    ShowData() #顯示排序後資料
