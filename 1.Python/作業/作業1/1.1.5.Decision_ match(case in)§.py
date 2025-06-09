#使用 try...except 判斷、ShowGrade(score)顯示成績 [使用 in array]
import numpy as np


def ShowGrade(score):
    a=np.arange(0,10)   #[0 1 2 3 4 5 6 7 8 9]
    #a=list(range(0,10)) #[0 1 2 3 4 5 6 7 8 9] #list無法運算(+90)
   
    match score:
        case score if score > 100.0 or score < 0.0 :
           msg = "請輸入 0-100 範圍的數字!"
        case score if score in (90+a) or score==100:
            print(90+a)
            msg = "A級"
        case score if score in (80+a):
            msg = "B級"
        case score if score in (70+a):
            msg = "C級"
        case score if score in (60+a):
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