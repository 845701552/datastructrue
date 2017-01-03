#coding:utf-8
"""
插入排序算法python实现
"""

def insert_sort(lst):
    """
    插入排序算法python实现
    """
    for i in range(1,len(lst)):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]:#和前一个比较发现逆序
                lst[j-1],lst[j]=lst[j],lst[j-1]#交换
            else:
                break#跳出内层循环

if __name__=="__main__":
    lst=[3,5,9,8,4,2,1,0,-6,12,-8]
    insert_sort(lst)
    print lst

