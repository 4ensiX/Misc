def qsort(list,r):
    if len(list) <= 1:
        return list
    else:
        if list[0] < list[1]:
            pivot = list[1]
        else:
            pivot = list[0]
        xlist = [x for x in list if x != pivot]
        less = qsort([x for x in xlist if x < pivot],r)
        greater = qsort([x for x in xlist if x > pivot],r)
        if r == 0:#nomal mode greater
            return less + [pivot] + greater
        else:#reverse mode less
            return greater + [pivot] + less