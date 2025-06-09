sum = 0

def show(n):
    print("第 " + str(n) + " 次執行迴圈")
    
for i in range(1,11):   #range(1,11) 跑10圈； range(11) 0,1,2....10 跑11圈
    show(i)
    sum += i
print("1+2+...+10 = " + str(sum))
input("Press any key to exit.")
