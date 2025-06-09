import random as rm

def GetScore(x) :           #回傳單一學生資料
    rng1, rng2 = 40, 100
    tot=0
    list1=[]
    list1.append(x)                     #學號加入list
    for i in range(3):
        sco=rm.randint(rng1, rng2)      #產生單科成績
        list1.append(sco)               #逐個科目加入list
        tot+=sco                        #個人總分累計
    avg=round(tot/3,1)                  #個人平均
    list1.extend([tot, avg])            #list同時加多個元素
    return list1                        #回傳list

def ShowData(lists):
    #顯示資料
    print("\n學號  國文  數學   英文  總分  平均")
    for i in range(0, len(lists)):          #r=len(lists)
        for j in range(0,len(lists[1])):    #c=len(lists[1])
            if j==0:
                print(f'{lists[i][j]:3}', end="")   #
            elif j==5:
                print(f'{lists[i][j]:6.1f}', end="")
            else:
                print(f'{lists[i][j]:6}', end="")

            #因lists=[],需使用lists[i][j]，不能使用lists[i,j]
        print()
    print()


#main主程式
n=5         #指派人數
lists=[]    #宣告 list (串列)
for i in range(0, n):
    list2=GetScore(i+1)     #學號由1開始 list2為一筆學生資料
    lists.append(list2)     #list2加入二維lists

print(lists)        #直接顯示串列內容
print()

for item in lists:  #迴圈顯示內容
    print(item)

ShowData(lists)     #使用自訂方法顯示內容








'''
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
    print(listname[i].ljust(3), str(i+1).rjust(5), str(listchinese[i]).rjust(5),
          str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))
'''