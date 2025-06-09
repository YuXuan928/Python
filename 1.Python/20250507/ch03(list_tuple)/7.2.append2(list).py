
#使用 list(map(int, input(...).split()))
#92 88 86 78 91 75 82 75
score = list(map(int, input("請輸多個入成績：<空格分隔>").split()))  #返回結果是一個列表  list 輸入一個字列串
total=sum(score)
average = total / len(score)
print(f"總成績:{total}； 平均成績:{average:.2f}")  #.2f 也是取到小數第二位的表示法
print(sum(score))
print(sum(score)/len(score))
