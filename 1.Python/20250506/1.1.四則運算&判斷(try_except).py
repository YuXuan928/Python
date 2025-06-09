#使用 try except文字判斷回傳

def try_except(x):
    tf=True
    try:
        x=int(x)
    except :            #ValueError
        tf=False    
    return tf
    
while (True):    
    a=input("請輸入整數 a：")
    if try_except(a)==False:
        print(f"輸入值a={a}不是數字!")
        continue
    else: break
    
while (True):    
    b=input("請輸入整數 b：")
    if try_except(b)==False:
        print(f"輸入值b={b}不是數字!")
        continue
    else: break
        
print()
a=int(a)
b=int(b)
print("a + b = " + str(a+b))
print("a - b = " + str(a-b))
print("a * b = " + str(a*b))
print("a / b = %.3f(值)； 商=%d； 餘數=%d #百分比法" % (a/b, a//b, a%b))  #百分比(%)
print("a / b = {:.3f}(值)； 商={:d}； 餘數={:d} #str.format()表示法".format(a/b, a//b, a%b))  #str.format()表示法
print("a / b = " + f'{a/b:.3f}(值)； 商={a//b}； 餘數={a%b} #f-string表示法')

input("Press any key to exit.")

