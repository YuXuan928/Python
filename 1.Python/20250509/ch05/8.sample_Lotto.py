
import random as r

list1 = r.sample(range(1,50), 7)        #從1-49的樣品中隨機取7個(不重複)
special = list1.pop()                   #第1個為特獎取出(剩6個)
list1.sort()                            #將6個中獎號碼排序
print("本期大樂透中獎號碼為：", end="")
for i in range(0,6):
    if i == 5:    print(str(list1[i]))      #第6個不加逗號及空格
    else:    print(str(list1[i]), end=", ") #前5個加逗號及空一格
print("本期大樂透特別號為：" + str(special)) #特獎號碼
