#coding:utf-8
def quick_sort(lst):
    qsort_rec(lst,0,len(lst)-1)
def qsort_rec(lst,l,r):
    if l>r:return 
    i=l
    j=r
    temp=lst[i]#tempΪ��ʱ������ʹ��lst[i]Ϊ��ʼ��λ
    while i<j:#�ҵ�temp������λ��
        while i<j and lst[j]>=temp:#���������ҵ���һ����tempС����
            j-=1
        if i<j:#�ҵ���tempС������lst[j]�����ƣ��ұ߳��ֿ�λ��i+1��ʼ�ұ�temp�������
            lst[i]=lst[j]
            i+=1
        while i<j and lst[i]<=temp:#���������ҵ���һ����temp�����
            i+=1
        if i<j:
            lst[j]=lst[i]#�ҵ��ֱ�temp�������lst[i]�ƶ����ұߣ���߳��ֿ�λ��j-1��ʼ�ұ�tempС����
            j-=1
    lst[i]=temp#temp�������յ�λ��
    qsort_rec(lst,l,i-1)#�ݹ�����������
    qsort_rec(lst,i+1,r)#�ݹ�����Ұ�����