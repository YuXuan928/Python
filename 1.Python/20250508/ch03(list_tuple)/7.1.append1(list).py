score = []              #建立空串列
total = inscore = 0
# while(inscore != -1):
#     inscore = int(input("請輸入學生的成績：<結束 -1>"))
#     score.append(inscore)


score=[92,88,86,78,90,-1]
score=score[:-1]    #最後結束-1會被納入
print(score)

print("共有 %d 位學生" % (len(score)))
for i in range(0, len(score)): 
    total += score[i]
average = total / (len(score))
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

input("Press any key to exit.") 