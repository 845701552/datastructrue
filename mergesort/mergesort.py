#coding:utf-8

def mergesort(seq):
    """
    归并排序算法python实现
    """
    if len(seq)<=1:#将序列不断分为小切片
        return seq
    mid=int(len(seq)/2)
    left=mergesort(seq[:mid])
    right=mergesort(seq[mid:])
    return merge(left,right)#第一次传过去的是[left=5,right=4],第二次传过去的是[left=7,right=4,5]
def merge(left,right):
    """
    比较传过来的两个序列left,right，返回一个排好的序列
    """
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]#这时候i或者j到了序列的最后
    result+=right[j:]
    return result

if __name__=="__main__":
    seq=[7,5,4,9,7,5,1,0,7,-2,3,-99,6]
    res=mergesort(seq)
    print res