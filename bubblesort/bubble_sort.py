# coding:utf-8
"""
这个.py文件实现冒泡排序
"""
def bubble_sort(lst):
    """
    冒泡排序python实现
    """
    for i in range(len(lst)):#i从0到7遍历
        flag=True;#设置变量flag，发现是否已经有序
        for j in range(1,len(lst)-i):#j从1到len(lst)-i
            if lst[j-1]>lst[j]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
                flag=False
        if flag:#序列本来就有序，故退出
            break;
if __name__=="__main__":
    lst=[30,13,25,16,47,26,19,10]
    print lst
    bubble_sort(lst)
    print lst

