for i in range(1,10):
    for j in range(1,10):
        product = i * j
        #print("%d*%d=%2d   " % (i, j, product), end="") #=%-2d 改=%2d 對齊
        print(f"{j}*{i}={i*j:2d}", end="   ") #f=string 同上
    print()
input("Press any key to exit.") 
