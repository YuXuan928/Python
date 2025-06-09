score = [85, 79, 93]
#單項逐一print()顯示
print("*多個print())顯示")
print("國文成績：%d 分" % score[0])
print("數學成績：%d 分" % score[1])
print("英文成績：%d 分" % score[2])


#使用迴圈顯示
print("#1.使用 in range() 顯示")
for i in range(len(score)):
    print(i, score[i])

print("\n#2.使用 in object 顯示")  
i=0
for value in score:     #Iterable (可疊代的)物件
    print(i, value)
    i+=1
    
print("\n#3.使用 in enumerate(list) 顯示")  
for i, val in enumerate(score):
    print(i, value)
    
input("Press any key to exit.")