innum = 0
list1 = []
while(innum != -1):
    innum = int(input("請輸入電費 (-1：結束)："))
    list1.append(innum)
list1.pop()
print("共輸入 %d 個數" % len(list1))
print("最多電費為：%d" % max(list1))
print("最少電費為：%d" % min(list1))
print("電費總和為：%d" % sum(list1))
print("電費由大到小排序為：{}".format(sorted(list1, reverse=True)))
#sorted() 是 Python 的內建排序函式，會傳回一個排序後的新串列，而不會改變原本的 list1
# list1 是我們存放電費資料的清單。
# reverse=True 表示'反向'排序，也就是從大到小排列（預設是從小到大）。

