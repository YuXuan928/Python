def Multi99():
    st=""
    for i in range(1,10):
        for j in range(1,10):
            st+=f"{j}*{i}={i*j:2d}   "
            #print(f"{j}*{i}={i*j:2d}", end="   ") #f=string 同上
        st+="\n"
        
    return st

print(Multi99())
input("Press any key to exit.") 
