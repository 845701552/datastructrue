#coding:UTF-8  

def fixdown(a,k,n):
    """
    ���ϵ������У�ʹ�����г�Ϊ�����
    """
    N=n-1
    while 2*k<=N:
        j=2*k#j��k�ڵ���ӽڵ�
        if j<N and a[j]<a[j+1]:#j�������һ���ڵ�,�������ӽڵ�Ƚϴ�С,a[j]�������ӽڵ�
            j+=1
        if a[k]<a[j]:#�ȽϽϴ��ӽڵ�a[j]�͸��ڵ��ֵ
            a[k],a[j]=a[j],a[k]#����
            k=j#�����󣬿�ʼ�������¼���ӽڵ��С
        else:
            break
def heapsort(l):
    """
    ������pythonʵ��
    """
    n=len(l)-1
    for i in range(n//2,0,-1):#i�ķ�ΧΪ5,4,3,2,1û��0
        fixdown(l,i,len(l))#ִ�е���������ֵ77�Ѿ������
    while n>1:
        l[1],l[n]=l[n],l[1]#������β����Ԫ�طŵ��Ѷ�λ�ã�
        fixdown(l,1,n)#�����д������гɴ����
        n=n-1#���Ͻ��Ѷ�Ԫ��ȡ��
    return l[1:]#��������������


if __name__=="__main__":  
    l=[-1,26,5,77,1,61,11,59,15,48,19]#��һ��Ԫ�ز��ã�ռλ  
    print l
    res=heapsort(l)
    print res 
