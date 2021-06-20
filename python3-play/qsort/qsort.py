def qsort(lst,r):
    if len(lst) <= 1:
        return lst
    else:
        #if lst[0] < lst[1]:
        #    pivot = lst[1]
        #else:
        #    pivot = lst[0]
        #xlst = [x for x in lst if x != pivot]
        pivot = lst[0]
        xlst = lst[1:]
        less = qsort([x for x in xlst if x <= pivot],r)
        greater = qsort([x for x in xlst if x > pivot],r)
        if r == 0:#nomal mode greater
            return less + [pivot] + greater
        else:#reverse mode less
            return greater + [pivot] + less