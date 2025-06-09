score = 0;
while (score != -1):
    score = int(input("請輸入成績<結束 -1>："))
    if score == -1:
        continue        #同break;
    if(score) >= 90:
        print("優等")
    elif(score) >= 80:
        print("甲等")
    elif(score) >= 70:
        print("乙等")
    elif(score) >= 60:
        print("丙等")
    else:
        print("丁等")
input("Press any key to exit.")