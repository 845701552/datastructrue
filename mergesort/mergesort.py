#coding:utf-8

def mergesort(seq):
    """
    �鲢�����㷨pythonʵ��
    """
    if len(seq)<=1:#�����в��Ϸ�ΪС��Ƭ
        return seq
    mid=int(len(seq)/2)
    left=mergesort(seq[:mid])
    right=mergesort(seq[mid:])
    return merge(left,right)#��һ�δ���ȥ����[left=5,right=4],�ڶ��δ���ȥ����[left=7,right=4,5]
def merge(left,right):
    """
    �Ƚϴ���������������left,right������һ���źõ�����
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
    result+=left[i:]#��ʱ��i����j�������е����
    result+=right[j:]
    return result

if __name__=="__main__":
    seq=[7,5,4,9,7,5,1,0,7,-2,3,-99,6]
    res=mergesort(seq)
    print res