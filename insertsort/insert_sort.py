#coding:utf-8
"""
���������㷨pythonʵ��
"""

def insert_sort(lst):
    """
    ���������㷨pythonʵ��
    """
    for i in range(1,len(lst)):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]:#��ǰһ���ȽϷ�������
                lst[j-1],lst[j]=lst[j],lst[j-1]#����
            else:
                break#�����ڲ�ѭ��

if __name__=="__main__":
    lst=[3,5,9,8,4,2,1,0,-6,12,-8]
    insert_sort(lst)
    print lst

