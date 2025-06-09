n=1
while (n>0):
    n = int(input("請輸入大於1且小於101的正整數：<結束:0>"))
    if n<=0:
        continue
    n=2 if n==1 else n      #類似C#三元判斷 若n=1 會強制讓n=2
    n=100 if n>100 else n   #若n<100 會強制讓n=100
    
    #st=""
    #sum = 0
    #--下式同上二式
    st, sum = "", 0         #多重指派
    for i in range(1, n+1):
        st+=f"{i:2d}+"  #字串顯示2位數空間和+號
        sum += i
        if(i%10==0):  #如果整行數字超過十個數就會自動換行
            st+="\n"  #\n自動換行
    st=st[0:len(st)-2]     #去末位 '+''取st的字串長度並往前2個長度'(由分號後的正負數決定往前還是往後取)
    #st=st[:-2]                 #功能同上
    print(st+"="+str(sum))
    print("1 到 %d 的整數和為 %d" % (n, sum))
    