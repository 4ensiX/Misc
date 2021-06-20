from qsort import *

num=[]
for i in range(5):
    num.insert(i,input())

num2= qsort([int(n) for n in num],0)
num3 = qsort([int(n) for n in num],1)
num.sort(key=int)

print(num2)
print(num3)
print(num)


