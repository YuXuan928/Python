listname = ["林大明", "陳阿中", "張小英"]
listchinese = [100, 74, 82]
listmath = [87, 88, 65]
listenglish = [79, 100, 8]
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
    print(listname[i].ljust(5), str(i+1).rjust(3), str(listchinese[i]).rjust(5),
          str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))


# =============================================================================
# for i in range(0,3):
#     print(listname[i].ljust(5),         # 姓名靠左對齊，寬度5
#           str(i+1).rjust(3),            # 座號靠右對齊，寬度3（座號從 1 開始）
#           str(listchinese[i]).rjust(5),# 國文成績靠右對齊，寬度5
#           str(listmath[i]).rjust(5),   # 數學成績靠右對齊，寬度5
#           str(listenglish[i]).rjust(5))# 英文成績靠右對齊，寬度5
# 🔠 .ljust() 與 .rjust() 說明：
# ljust(n): 讓字串「靠左對齊」，整體寬度為 n 個字元。
# 
# rjust(n): 讓字串「靠右對齊」，整體寬度為 n 個字元。
# =============================================================================

