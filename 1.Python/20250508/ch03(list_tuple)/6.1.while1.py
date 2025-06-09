total = person = score = 0
while(score != -1):
    person += 1
    total += score
    score = int(input("請輸入第 %d 位學生的成績<結束-1>：" % person))
average = total / (person - 1)
#print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))
print(f"本班共{person-1}人； 總成績：{total} 分 ；平均成績：{average:5.2f} 分") 
input("Press any key to exit.") 