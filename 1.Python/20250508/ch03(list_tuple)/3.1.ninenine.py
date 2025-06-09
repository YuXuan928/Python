for i in range(1,10):
    for j in range(1,10):
        product = i * j
        #print("%d*%d=%-2d   " % (i, j, product), end="")   #靠左未對齊
        print("%d*%d=%2d   " % (i, j, product), end="")     #靠右對齊
    print()
input("Press any key to exit.") 
