pd= []
vd = []

for i in range(3):
    pd.append(int(input()))

pst = int(input())
pend = int(input())  

for i in range(3):
    vd.append(int(input()))

vst = int(input())
vend = int(input())

def Work(pd,vd,pst,pend,vst,vend,Value = 0):    
    if(abs(pst-vst)>1):
        return 0
    if(abs(pend-vend)>1):
        return 0
    for i in range(3):
        for n in range(3):
            if (pd[i]==vd[n]):
                Value += 1   
    return Value

print(Work(pd,vd,pst,pend,vst,vend))
