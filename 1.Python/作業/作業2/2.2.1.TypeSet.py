
#str完原字串； nmu為新字串的總長度； padchar填加的字元
def PadLeft(str, num, padchar): #本函數僅作參考(如C#PedLeft(, ,))，本題未使用
    stringlength = len(str)
    n = num - stringlength
    if n >= 0:
        str = padchar*n + str
    return str

def Q1_Q2(q) :      #水平遞增, 正立
    n=5
    s1=s2=s3=''
    c=48 if (q==1) else 64
    for i in range(1,n+1):
        #print(s*i, end="")     #同 print(PadLeft('', i-1, '  '), end="")
        s1+=""*(n-i)            #垂直遞增變數會在'i'
        s2+=" "*(n-i)
        s3+="  "*(n-i)
        for j in range(1,i+1):
            s1 += str(chr(j+c)) + " "   #print(j,end=" ")
            s2 += str(chr(j+c)) + " "   #水平遞增變數會在'j'
            s3 += str(chr(j+c)) + " "
        s1+="\n";   s2+="\n";   s3+="\n"

    return s1+s2+s3

def Q3_Q4(q) :      #垂直遞增, 正立
    n=5
    s1=s2=s3=''
    c=48 if (q==3) else 64
    for i in range(1,n+1):
        #print(s*i, end="")    #同 print(PadLeft('', i-1, '  '), end="")
        s1+=""*(n-i)
        s2+=" "*(n-i)
        s3+="  "*(n-i)
        for j in range(1,i+1):
            s1 += str(chr(i+c)) + " "   
            s2 += str(chr(i+c)) + " "   
            s3 += str(chr(i+c)) + " "
        s1+="\n";   s2+="\n";   s3+="\n"

    return s1+s2+s3

def Q5_Q6(q):       #水平遞增, 倒立  需要一固定數去減
    n=5
    s1=s2=s3=''
    c=48 if (q==5) else 64
    for i in range(1,n+1):
        #print(s*i, end="")   #同 print(PadLeft('', i-1, '  '), end="")
        s1+=""*(i-1)
        s2+=" "*(i-1)
        s3+="  "*(i-1)
        for j in range(1,n-i+2):
            s1 += str(chr(j+c)) + " "   #print(j,end=" ")
            s2 += str(chr(j+c)) + " "   
            s3 += str(chr(j+c)) + " "
        s1+="\n";   s2+="\n";   s3+="\n"

    return s1+s2+s3




#main
while (True):
    #題目選項
    x=int(input("請選擇： (1)第1題 (2)第2題 (3)第3題 (4)第4題 (5)第5題  (6)第6題 (0)結束 "))
    st=""
    if (x < 0 or x > 6):
        print("請輸入 0-6 之間的數")
        continue
    elif (x == 0):
        break
    elif (x == 1 or x == 2):
        title='1. 水平遞增, 正立, 數字'  if(x==1) else '2. 水平遞增, 正立, 英文字' 
        st=Q1_Q2(x)        
    elif (x == 3 or x == 4):
        title='3. 垂直遞增, 正立, 數字'  if(x==3) else '4. 垂直遞增, 正立, 英文字' 
        st=Q3_Q4(x)  
    elif (x == 5 or x == 6):
        title='5. 水平遞增, 倒立, 數字'  if(x==5) else '6. 水平遞增, 倒立, 英文字' 
        st=Q5_Q6(x)         
    #else:
    #    st=""
    print(title+"\n"+st)