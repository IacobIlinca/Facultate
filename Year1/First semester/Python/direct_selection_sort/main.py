l = [12,7,8,35,9]
def direct_selection_sort(l):
    for i in range (0, len(l)-1):
        for j in range (i+1, len(l)):
            if l[j]<l[i]:
                l[i],l[j] = l[j],l[i]

def insert_sort(l):
    for i in range(1, len(l)):
        ind = i-1
        a = l[i]
        while ind>=0 and a<l[ind]:
            l[ind+1] = l[ind]
            ind = ind-1
        l[ind+1] = a

def bubble_sort(l):
    sorted = False
    while not sorted:
        sorted = True
        for i in range (len(l)-1):
            if l[i+1]<l[i]:
                l[i],l[i+1] = l[i+1], l[i]
                sorted = False

def bubble_sort2(l):
    for j in range(1, len(l)):
        for i in range(len(l)-j):
            if l[i+1]<l[i]:
                l[i], l[i+1] = l[i+1], l[i]

def quick_sort(l):
    if len(l)<=1:
        return l
    pivot = l.pop()
    lesser = quick_sort([x for x in l if x<pivot])
    greater = quick_sort([x for x in l if x>=pivot])
    return lesser+[pivot]+greater       #a creat o lista noua, rezultatul din ea va fi diferit de forma finala a lui l!!


def partition(l,left,right):
    pivot = l[left]
    i = left
    j = right
    while i!=j:
        while l[j]>=pivot and i<j:
            j = j-1
        l[i] = l[j]
        while l[i]<=pivot and i<j:
            i=i+1
        l[j] = l[i]
    l[i] = pivot
    return i

def quickSort_rec(l,left,right):
    pos = partition(l, left, right)
    if left<pos-1:
        quickSort_rec(l,left, pos-1)
    if pos+1<right:
        quickSort_rec(l,pos+1,right)


def merge_nu(l, left, right, m):
    n1 = m-left+1
    n2 = right-m
    L = [0]*n1
    R = [0]*n2

    for i in range (0,n1):
        L[i] = l[left+1]
    for j in range (0,n2-1):
        R[j] = l[m+1+j]

    i = 0
    j = 0
    k = left
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            l[k] = L[i]
            i = i+1
        else:
            l[k] = R[j]
            j = j+1
        k = k+1
    while j<n2-1:
        l[k] = R[j]
        j = j+1
        k = k+1
    while i<n1-1:
        l[k] = L[i]
        i = i+1
        k = k+1

def merge(l, left,right,m):
    aux = [None]*len(l)
    i = left
    j = m+1
    k = left
    while i<=m and j<=right:
        if l[i]<l[j]:
            aux[k] = l[i]
            i = i+1
            k = k+1
        else:
            aux[k] = l[j]
            j = j+1
            k = k+1
    while i<=m:
        aux[k] = l[i]
        i = i + 1
        k = k + 1
    while j<=right:
        aux[k] = l[j]
        j = j + 1
        k = k + 1
    for i in range (left, right+1):
        l[i] = aux[i]


def merge_sort(l,start,end):
    if end-start<=1:
        return
    m=(end+start)//2
    merge_sort(l,start,m)
    merge_sort(l,m+1,end)
    merge(l,start,end,m)

def search_seq_chei_ordonate(el,l):
    if len(l) == 0: return 0
    # if el<=l[0]:return 0
    # if el>=l[len(l)-1]: return len(l)

    ind = -1
    for i in range(0,len(l)):
        if el<=l[i]:
            ind=i

    if ind == -1: return len(l)
    return ind

print("nu")
list = quick_sort(l)
el = 8
print(search_seq_chei_ordonate(el,list))
#print(l)
print("da")
#merge_sort(l,0,len(l)-1)
#quickSort_rec(l,0,len(l)-1)
#print(quick_sort(l))
#bubble_sort2(l)
#bubble_sort(l)
#insert_sort(l)
#direct_selection_sort(l)
