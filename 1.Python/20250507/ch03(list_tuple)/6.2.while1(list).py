import statistics   #統計應用模組
import numpy as np  #numpy應用模組

total = person = score = 0
list=[]
i=1
while(score != -1):
    score = int(input("請輸入第 %d 位學生的成績<結束-1>：" % i))
    if(score == -1):
        continue
    list.append(score)
    i+=1
  
person=len(list)            #人數
total=sum(list)             #總和
average = total / person    #平均1 sum(list)/len(list)
statistics.mean(list)       #平均2 statistics
average = np.mean(list)     #平均3 numpy


for i in range(person):
    print(f"list[{i}]={list[i]}")   #list+[i值]={i值}   {}用於表示 字典(dict)這種資料結構，我們會使用大括號框住資料

#print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))   %5.2f 指的是字列串空間有五格，取到小數第二位(有含小數點)
print(f"本班共{person}人； 總成績：{total} 分 ；平均成績：{average:5.2f} 分") 
input("Press any key to exit.") 