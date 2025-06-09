money = 1
while money != 0:
    money = int(input("請輸入購物金額 <結束 0>："))
    if money == 0:
        continue
    if(money >= 100000):
        d = 0.8             #八折
    elif(money >= 50000):
        d = 0.85            #八五折
    elif(money >= 30000):
        d = 0.9             #九折
    elif(money >= 10000):
        d = 0.95            #九五折
    else:
        d = 1               #未打折
    s= '無折扣' if d==1 else f'{d*100:.0f}折'
    print(f"折扣：{s}  金額：{money * d} 元\n") #九五折
input("Press any key to exit.")