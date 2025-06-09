def Multi99():
    st1=st2=st3=''
    for i in range(1, 10):
        for j in range(1, 10):
            st1 += "%d*%d=%2d  " % (j, i, i*j) #使用百分比格式化
            st2 += "{:d}×{:d}={:2d}  ".format(j, i, i*j)  # 使用str.format()格式化
            st3 += f"{j}*{i}={i*j:2d}  "   ## 使用f string 格式化
        st1 += '\n';  st2 += '\n';  st3 += '\n'
    return st1, st2, st3

#main
list = Multi99()
ttl=['(1)百分比(%)表示法', '(2)str.format()表示法', '(3)f-string表示法']
for i in range(len(list)):
    print(f'{ttl[i]}\n{list[i]}')

#input("Press any key to exit.") 
