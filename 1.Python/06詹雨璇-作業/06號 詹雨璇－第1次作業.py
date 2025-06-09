#實用級
#1.match
score = 1
data = ""
while (score != -1):
    score = float(input("請輸入成績 <結束 -1>："))
    if (score ==-1):break
    if (score >100 and score <0):
       s = "請輸入 0-100 的數字！"

    grade =1 if(score >= 90 and score<=100) else 2 if(score >= 80 and score<90) else 3 if(score>=70 and score<80) else 4 if(score>=60 and score<70) else 5 if (score >=0 and score<60) else 6

    match grade :
        case 1:d="A級"
        case 2:d="B級"
        case 3:d="C級"
        case 4:d="D級"
        case 5:d="E級"
        case _:d="請輸入 0-100 的數字！"
    s='' if d==1 else f'{d}'
    print(f"{score} : {d}\n") #成績等級評斷
    
#進階級
#2. if..else
def grade(score):
    if (score > 100.0 or score < 0.0):
       print("請輸入 0-100 範圍的數字!")
    elif(score >= 90):
        d = "A級"
    elif(score >= 80):
        d = "B級"
    elif(score >= 70):
        d = "C級"
    elif(score >= 60):
        d = "D級"
    else:
        d = "E級"
    print(f"成績：{score}； 等級：{d}") 


data = ""
while data != "-1":
    data = input("請輸入成績 <結束 -1>：")
    if data=="":
        data="0"
        continue
    try:
        score = float(data)
        if score == -1 :
            break;       #結束
        grade(score)
    except ValueError:
        print("輸入值不是數字!")  
        
#九九乘法
#基礎級
for i in range(1,10):
    for j in range(1,10):
        print(f"{j}*{i}={i*j:2d}", end=" |") 
    print()

#實用級
def data():
    st=""
    for i in range(1,10):
        for j in range(1,10):
            st+=f"{j}*{i}={i*j:2d} |"
        st+="\n"        
    return st
print(data()) 





































        
        