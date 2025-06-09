
#使用 list(map(int, input(...).split()))
#92 88 86 78 91 75 82 75
score = list(map(int, input("請輸多個入成績：<空格分隔>").split()))
total=sum(score)
average = total / len(score)
print(f"總成績:{total}； 平均成績:{average:.2f}")
print(sum(score))
print(sum(score)/len(score))
