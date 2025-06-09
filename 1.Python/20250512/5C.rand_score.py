import random as rm

listname = ["林大明", "陳阿中", "張小英"]
i=0
list=[]
while (i<9):
    list.append(rm.randint(40,100)) #40 <= x <= 100
    i+=1
print(f"亂數：{list}")
listchinese = list[:3]      #前3項  index[0,1,2]
listmath = list[3:-3]       #index4開始到末3項-3，index[3,4,5]
listenglish = list[-3:]     #後3項  index[6,7,8]

print("國文：",end=" ")
print(listchinese)
print("數學：",end=" ")
print(listmath)
print("英文：",end=" ")
print(listenglish)
print()
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
    print(listname[i].ljust(3), str(i+1).rjust(5), str(listchinese[i]).rjust(5),
          str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))
