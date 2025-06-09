from datetime import datetime    #第一個 datetime 是模組名稱，第二個是類別名稱。
date0 = "2017-8-23"         #日期(字串型態)

date1 = "西元 " + date0
date1 = date1.replace("-", " 年 ", 1) #替換不超過1次，本案例可以不使用第3個參數
date1 = date1.replace("-", " 月 ", 1) #替換不超過1次，本案例可以不使用第3個參數
date1 += " 日"
print("#使用文字型態作 replace( , , )")
print(date1)


date2=datetime.strptime(date0, '%Y-%m-%d')  #日期(日期型態)
print("#使用日期型態取 year,month,day")
print(f"西元 {date2.year} 年 {date2.month} 月 {date2.day} 日")

# =============================================================================
# data.replace 說明
# ===============================
# date1.replace("-", " 年 ", 1)
# replace(old, new, count) 是 Python 字串的內建方法：
# 
# old：要被取代的子字串（這裡是 "-"）
# 
# new：取代成的新字串（這裡是 " 年 "）
# 
# count=1：只取代第一次出現的 "-"（若不寫，預設會全部取代）
# =============================================================================
