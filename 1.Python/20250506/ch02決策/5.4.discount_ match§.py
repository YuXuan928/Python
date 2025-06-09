money = 1
while money != 0:
    money = int(input("請輸入購物金額 <結束 0>："))
    mon=int(money/10000)    #只取整數部份
    c=1 if(mon >= 10) else 2 if(mon >= 5) else 3 if(mon>=3) else 4 if(mon>=1) else 5
    
    match c :
        case 1:d=0.8
        case 2:d=0.85
        case 3:d=0.9
        case 4:d=0.95
        case _: d=1
    s= '無折扣' if d==1 else f'{d*100:.0f}折'
    print(f"折扣：{s}  金額：{money * d} 元\n") #九五折
input("Press any key to exit.")