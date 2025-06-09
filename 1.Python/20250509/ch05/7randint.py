import random as r

while True:
    inkey = input("按任意鍵再按[ENTER]鍵擲骰子，直接按[ENTER]鍵結束:")
    if len(inkey) > 0:
        num = r.randint(1,6)    # 1 <= x <= 6
        print("你擲的骰子點數為：" + str(num))
    else:  
        print("遊戲結束！")
        break

# =============================================================================
# randint() 是用來產生隨機整數的函式，來自 random 模組。
# 
# 🔹 語法：
#
# from random import randint
# 
# randint(a, b)
#
# 產生一個  "介於 a 和 b（含頭含尾"  的整數。
# 
# 換句話說，a ≤ 隨機數 ≤ b    
# =============================================================================
