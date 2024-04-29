import math

Len = int(input())
Vmoney,Pmoney = [],[]
for i in range(Len):
    Vmoney.append(int(input()))
for i in range(Len):
    Pmoney.append(int(input()))

print("Зарплата:",sum(Vmoney)) 
print("Зарплата:",sum(Pmoney))

if sum(Vmoney) > sum(Pmoney):
    print(math.ceil((sum(Vmoney) - sum(Pmoney))/Pmoney[Len-1]),"Дней")
else:
    print(math.ceil((sum(Pmoney) - sum(Vmoney))/Vmoney[Len-1]),"Дней")
