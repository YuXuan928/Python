#使用 try...except 判斷、ShowGrade(score)顯示成績
#import sys
def ShowGrade_if_elif(score):
    if(score > 100.0 or score < 0.0):
       msg = "請輸入 0-100 範圍的數字!"
    elif(score >= 90):
        msg = "A級"
    elif(score >= 80):
        msg = "B級"
    elif(score >= 70):
        msg = "C級"
    elif(score >= 60):
        msg = "D級"
    else:
        msg = "E級"
    print(f"成績：{score}； 等級：{msg}") 
    
def ShowGrade_case(score):
    if(score > 100.0 or score < 0.0):
       msg = "請輸入 0-100 範圍的數字!"
    else:
        s=int(score/10)
        c=1 if(s>=9) else 2 if(s>=8) else 3 if(s>=7) else 4 if(s>=6) else 5
        match c :
            case 1:msg="A級"
            case 2:msg="B級"
            case 3:msg="C級"
            case 4:msg="D級"
            case _:msg="E級"
    print(f"成績：{score}； 等級：{msg}") 
    

data = msg = ""
while data != "-1":
    data = input("請輸入成績 <結束 -1>：")
    if data=="":
        data="0"
        continue
    try:
        score = float(data)
        if float(data) == -1 :
            continue;       #結束
        #ShowGrade_if_elif(score)
        ShowGrade_case(score)
    except : #ValueError:
        print("輸入值不是數字!")
#input("Press any key to exit.")