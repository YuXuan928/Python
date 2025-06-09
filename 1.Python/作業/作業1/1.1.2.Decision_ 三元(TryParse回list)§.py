#使用方含數判決 try...except 回傳list、 main()顯示成績
def floatTryParse(value):
    try:
        return [str(float(value)), True]  #傳回list
    except ValueError:
        return [value, False]           #傳回list


data = 0
msg=""
while True:
    data = input("請輸入成績 <結束 -1>：")
    if data=="":
        data="0.0"
        continue
    if data == '-1' :
        break;       #結束
        
    list1=floatTryParse(data)    #check 是否文數字
    if list1[1]==False :
        print("輸入值不是數字!")
        continue   #sys.exit()
    score=float(list1[0])
    if(score > 100.0 or score < 0.0):
       print("請輸入 0-100 範圍的數字!")
       continue
    else:
        msg="A級" if(score >= 90) else "B級" if(score >= 80) else "C級" if(score >= 70) else "D級" if(score >= 60) else "E級"    
    print(f"成績：{score}； 等級：{msg}") 
    
#input("Press any key to exit.")