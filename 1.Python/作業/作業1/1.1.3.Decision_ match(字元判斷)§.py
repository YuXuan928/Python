#import sys

def CharCheck(s):   #自訂自元判斷函數
    tf=True
    x=y=0
    for i in range(len(s)):
        if ord(s[i])==45:   #'-'
            x+=1
        if ord(s[i])==46:   #'.'
            y+=1
        if (not(ord(s[i]) >= 48  and ord(s[i]) <= 57 or (ord(s[i]) == 45 and x < 2) or (ord(s[i]) == 46 and y < 2)) ):
            tf=False
            return tf
    return tf            
    


#main()
msg=""
while True:
    data = input("請輸入成績 <結束 -1>：")
    if data=="":
        continue
    if data == '-1' :
        break;       #結束
      
    #使用CharCheck(data)
    tf1=CharCheck(data)
    if tf1==False :
        print("輸入值不是數字!")
        continue   #sys.exit() import sys
    score=float(data)
    
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
    print(f"{score}：{msg}") 
#input("Press any key to exit.")