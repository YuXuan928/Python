for i in range(1,10):
    for j in range(1,10):
        #print("%d*%d=%2d   " % (j, i, i*j), end="") #=%-2d 改=%2d 對齊
        print(f"{j}*{i}={i*j:2d}", end="   ") #f=string 同上
    print()
#input("Press any key to exit.") 
