def Work(pd,vd,pst,pend,vst,vend,Value = 0):    
    if(abs(pst-vst)>1):
        print("0")
        quit
    if(abs(pend-vend)>1):
        print("0")
        quit
    for i in range(3):
        for n in range(3):
            if (pd[i]==vd[n]):
                Value += 1   
    return Value
