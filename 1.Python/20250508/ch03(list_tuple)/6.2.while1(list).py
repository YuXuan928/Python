import statistics 
import numpy as np

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
    print(f"list[{i}]={list[i]}")

#print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))
print(f"本班共{person}人； 總成績：{total} 分 ；平均成績：{average:5.2f} 分") 
input("Press any key to exit.") 