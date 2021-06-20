N = 5

def qsort(list,r):
    if len(list) < 1:
        return list
    else:
        pivot = list[0]
        xlist = list[1:]
        less = qsort([x for x in xlist if x <= pivot],r)
        print(pivot)
        greater = qsort([x for x in xlist if x > pivot],r)
        print(greater)
        if r == 0:#nomal mode greater
            return less + [pivot] + greater
        else:#reverse mode less
            return greater + [pivot] + less

num=[]
#for i in range(N):
#  num.insert(i, input())

ans=qsort(int(n) for n in num,0)
#num.sort(key=int)

print(ans)