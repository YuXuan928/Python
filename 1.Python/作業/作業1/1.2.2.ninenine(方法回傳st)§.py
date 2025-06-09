def Multi99():
    st=""
    for i in range(1,10):
        for j in range(1,10):
            st+=f"{j}*{i}={i*j:2d}   "
        st+="\n"
        
    return st

print(Multi99())
#input("Press any key to exit.") 
