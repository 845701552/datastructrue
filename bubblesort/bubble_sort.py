# coding:utf-8
"""
���.py�ļ�ʵ��ð������
"""
def bubble_sort(lst):
    """
    ð������pythonʵ��
    """
    for i in range(len(lst)):#i��0��7����
        flag=True;#���ñ���flag�������Ƿ��Ѿ�����
        for j in range(1,len(lst)-i):#j��1��len(lst)-i
            if lst[j-1]>lst[j]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
                flag=False
        if flag:#���б��������򣬹��˳�
            break;
if __name__=="__main__":
    lst=[30,13,25,16,47,26,19,10]
    print lst
    bubble_sort(lst)
    print lst

