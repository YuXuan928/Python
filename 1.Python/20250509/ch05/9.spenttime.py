import time

start=(time.time())         # 開始執行時間 由1970.1.1到當前秒數
print("開始時間：{}" .format(start))
for i in range(100):        # i = 0 - 99
    time.sleep(0.001)       #暫停0.001秒
end=(time.time())           # 結束執行時間 由1970.1.1到當前秒數
print("結束時間：{}" .format(end))
print("使用時間：%7.3f 秒" %(end-start))