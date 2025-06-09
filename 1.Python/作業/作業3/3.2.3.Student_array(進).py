import random
import numpy as np

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
def GetRank(ary1):          #取得名次
    list1=[]
    for i in range(0,n):
        list1.append(ary1[i,4])

    list1.sort()                    #list排續(遞增)
    list1.reverse()                 #list排續(遞減)
    for i in range(n):              #於list(降冪排序)中找原ary1 總分
        x=list1.index(ary1[i,4])     
        ary1[i,6]=x+1               #寫入ary1名次    

#----------
def ShowData(array):
    #顯示資料
    csum=[0]*6  #宣告長度為6的全 0 list
    print("學號  國文  英文   數學  總分  平均   名次  不及格科數 ")
    for i in range(0, n): 
        #csum[j]=0
        for j in range(0,8):
            if j==0:
                print(f'{array[i,j]:3.0f}', end="")
            elif j==5:
                print(f'{array[i,j]:6.1f}', end="")
            elif j==7:
                print(f'{array[i,j]:8.0f}', end="")
            else:
                print(f'{array[i,j]:6.0f}', end="")
            if 0<j<6:
                csum[j]+=array[i,j]
            
        print()
    print("     ----  ----  ----  ----  ----")
    print('    ',end="")    #接下方學號位置(學號步累計-資料空白)
    for j in range(1,6):
        print(f'{csum[j]/n:5.1f}', end=' ')     #由國文...平均


#----------
#main主程式
n=int(input("請輸入學生人數："))
n=20 if n>20 else n
lst=[]  #宣告二維陣列
for i in range(0, n):
    list2=GetScore(i+1)     #學號由1開始
    lst.append(list2)       #僅差名次沒有資料

ary=np.array(lst)

GetRank(ary)                #取得名次
print(f'(2)type={type(ary)}')
ShowData(ary)               #顯示原資料

#排序欄位選擇
#lists.sort(key=lambda lists: lists[1], reverse=True) #原資料變
#sorted1 = sorted(lists, key=lambda x: x[4]) #原資料不變
while True:
    s=input("\n\n選擇排序欄位[學號,國文,英文,數學...：1-8], [結束：0]")
    if s=='':
        continue
    
    sel=int(s);
    if sel==0:
        break
    elif sel>8 or sel<0:
        print('請輸入 1-8 的正整數!')
        continue
    
    slist=['學號', '國文', '英文', '數學', '總分', '平均', '名次', '不及格科數']
    
    if sel==7 or sel==8:
        ary1 = ary[ary[:, sel-1].argsort()]     #numpy.array排序遞增
    else:
        ary1 =ary[ary[:, sel-1].argsort()[::-1]] #遞增[::-1] 則將索引順序反轉成降序排列。
    
    ad= '遞減' if sel<7 else '遞增'
    print(f"\n#顯示學生資料：{slist[sel-1]}{ad}")
    ShowData(ary1) #顯示排序後資料
   