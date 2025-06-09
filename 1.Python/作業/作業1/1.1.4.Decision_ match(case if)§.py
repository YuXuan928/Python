#使用 try...except 判斷、ShowGrade(score)顯示成績

def ShowGrade(score):
    match score:
        case score if score > 100.0 or score < 0.0 :
           msg = "請輸入 0-100 範圍的數字!"
        case score if(score >= 90):
            msg = "A級"
        case score if(score >= 80):
            msg = "B級"
        case score if(score >= 70):
            msg = "C級"
        case score if(score >= 60):
            msg = "D級"
        case _:
            msg = "E級"
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
        ShowGrade(score)
    except ValueError:
        print("輸入值不是數字!")
#input("Press any key to exit.")