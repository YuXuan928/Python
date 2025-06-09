
def s1 (n):
    
    global x, y, str 
    x="★"
    y="　"
    str=""
       
    for i in range(1, n+1):             #i = 行數變數
        str = "  "*(n-1);
    for k in range(1, n - i +1):    #k = 對齊用變數
        str += y                   
    for j in range(1, i+1):         #j = 字串用變數
        str += x + y               
    str += "\n"
    return( "(1)正三角形" + str )
print("\n")     

def s2 (n):
    
    global x, y, str 
    x="★"
    y="　"
    str=""
    
    for i in range(1, n+1):
        str = "";
    for k in range(1, i):  
        str += y                    
    for j in range(1, n - i+2):         
        str += x + y                
    str += "\n"
    return("(2)倒三角形" + str)
print("\n")


def s3 (n):
    
    global x, y, str 
    x="★"
    y="　"
    str=""
    
    for i in range(1, n+1):             #i = 行數變數
        str = "";
    for k in range(1, n - i +1):   
        str += y                   
    for j in range(1, i+1):         
        str += x + y                
        str += "\n"                     
    print(str)
    
    for i in range(2, n+1):
        str = "";
    for k in range(1, i):  
        str += y                   
    for j in range(1, n - i+2):         
        str += x + y                
    str += "\n"
    return("(3)菱形" + str)
print("\n")    


while (True):
    #畫星星
    s=input("請選擇, (1)正三角 (2)倒三角  (3)菱形  (0)結束 ")
    try:
        z=int(s)
    except ValueError:
        print("請勿輸入非數字!!!")
        continue
    if (z < 0 or z > 3):
        print("請輸入 0-3 之間的數!")
        continue
    elif (z == 0):
        break
    
    while True:
        m=input("請選擇入每邊星星數：")
        try:
            n=int(m)
            n = 3 if n<3 else 8 if n>8 else n
            break                  #確認資料合理後,離開小迴圈，準備排圖案
        except ValueError:
            print("請勿輸入非數字!!!")
            continue
        
    if z==1:
        print(s1(n))
    elif z==2:
        print(s2(n))
    else:
        print(s3(n))