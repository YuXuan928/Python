#str完原字串； nmu為新字串的總長度； padchar填加的字元
def PadLeft(str, num, padchar): #本函數僅作參考(如C#PedLeft(, ,))，本題未使用
    stringlength = len(str)
    n = num - stringlength  # 計算需要補幾個字元
    if n >= 0:              # 如果原始長度不足才補
        str = padchar*n + str   # 在左邊補上 padchar
    return str               # 回傳結果

def Q1_Q2(q) :      #正向水平遞增
    n=5
    s1=s2=s3=''
    c=48 if (q==1) else 64
    for i in range(1,n+1):
        #print(s*i, end="")  #同 print(PadLeft('', i-1, '  '), end="")
        s1+=""*(n-i)
        s2+=" "*(n-i)
        s3+="  "*(n-i)
        for j in range(1,i+1):
            s1 += str(chr(j+c)) + " "   #print(j,end=" ")
            s2 += str(chr(j+c)) + " "   
            s3 += str(chr(j+c)) + " "
        s1+="\n";   s2+="\n";   s3+="\n"
    
    return s1+s2+s3

def Q3_Q4(q) :      #正向垂直遞增
    n=5
    s1=s2=s3=''
    c=48 if (q==3) else 64
    for i in range(1,n+1):
        #print(s*i, end="")         #同 print(PadLeft('', i-1, '  '), end="")
        s1+=""*(n-i)
        s2+=" "*(n-i)
        s3+="  "*(n-i)
        for j in range(1,i+1):
            s1 += str(chr(i+c)) + " "   
            s2 += str(chr(i+c)) + " "   
            s3 += str(chr(i+c)) + " "
        s1+="\n";   s2+="\n";   s3+="\n"
    
    return s1+s2+s3

def Q5_Q6(q):       #倒立水平遞增
    n=5
    s1=s2=s3=''
    c=48 if (q==5) else 64
    for i in range(1,n+1):
        #print(s*i, end="")         #同 print(PadLeft('', i-1, '  '), end="")
        s1+=""*(i-1)
        s2+=" "*(i-1)
        s3+="  "*(i-1)
        for j in range(1,n-i+2):
            s1 += str(chr(j+c)) + " "   #print(j,end=" ")
            s2 += str(chr(j+c)) + " "   
            s3 += str(chr(j+c)) + " "
        s1+="\n";   s2+="\n";   s3+="\n"
    
    return s1+s2+s3

def Q7_Q8(q):       #倒立水平遞減
    n=5
    s1=s2=s3=''
    c=54 if (q==7) else 70
    for i in range(1,n+1):
        #print(s*i, end="")         #同 print(PadLeft('', i-1, '  '), end="")
        s1+=""*(i-1)
        s2+=" "*(i-1)
        s3+="  "*(i-1)
        for j in range(1,n-i+2):
            s1 += str(chr(c-j)) + " "   #print(j,end=" ")
            s2 += str(chr(c-j)) + " "   
            s3 += str(chr(c-j)) + " "
        s1+="\n";   s2+="\n";   s3+="\n"

    return s1+s2+s3

#-----------------------


#main
while (True):
    #題目選項
    select="請選擇 : (1)第1題  (2)第2題  (3)第3題  (4)第4題  (5)第5題\n"
    select+=" "*9+"(6)第6題  (7)第7題  (8)第8題  (0)結 束 "
    x=int(input(select))
    st=""
    if (x < 0 or x > 8):
        print("請輸入 0-8 之間的數")
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
    elif (x == 7 or x == 8):
        title='7. 水平遞減, 倒立,  數字'  if(x==7) else '8. 水平遞減, 倒立, 英文字' 
        st=Q7_Q8(x)         
    #else:
    #    st=""
    print(title+"\n"+st)