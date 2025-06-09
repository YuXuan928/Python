import math
def IsPrime(n):
    tf=True
    if(n == 2):
        tf=True
    else:
        for i in range(2, int(math.sqrt(n))+1):   #原range(2, n):
            if(n % i == 0):
                tf=False
                break
    return tf

n=2
while n>1:
    n =int(input("請輸入大於 1 的整數 <結束0或1>："))
    if IsPrime(n):
        print("%d 是質數！" % n)
    else:
        print("%d 不是質數！" % n)
    