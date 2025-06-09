web = input("請輸入網址：")
if web.startswith("http://") or web.startswith("https://"):
    print("輸入的網址格式正確！")
else:
    print("輸入的網址格式錯誤！")
    
#startswith() 是字串（str）的方法之一，用來判斷一個字串是否以指定的子字串開頭。    