#coding:utf-8
def quick_sort(lst):
    qsort_rec(lst,0,len(lst)-1)
def qsort_rec(lst,l,r):
    if l>r:return 
    i=l
    j=r
    temp=lst[i]#temp为临时变量，使得lst[i]为初始空位
    while i<j:#找到temp的最终位置
        while i<j and lst[j]>=temp:#从右往左找到第一个比temp小的数
            j-=1
        if i<j:#找到比temp小的数，lst[j]往左移，右边出现空位，i+1开始找比temp大的数，
            lst[i]=lst[j]
            i+=1
        while i<j and lst[i]<=temp:#从左往右找到第一个比temp大的数
            i+=1
        if i<j:
            lst[j]=lst[i]#找到乐比temp大的数，lst[i]移动到右边，左边出现空位，j-1开始找比temp小的数
            j-=1
    lst[i]=temp#temp放入最终的位置
    qsort_rec(lst,l,i-1)#递归调用左半区间
    qsort_rec(lst,i+1,r)#递归调用右半区间