#coding: utf-8

"""
pythonʵ��ȫ����
"""
def permutation(lst):
    """
    pythonʹ�õݹ�ʵ��ȫ����
    """
    if len(lst)==0 or len(lst)==1:
        return [lst]
    result=[]
    for i in lst:
        temp_list=lst[:]#��lst���鸳ֵ��temp_list
        temp_list.remove(i)#ɾ��
        temp=permutation(temp_list)#�ݹ�����ɾ��һ��Ԫ�غ��ȫ����
        for j in temp:#�������ɵ�ȫ����
            j.insert(0,i)#��ɾ����i��ӵ���ǰ��
            result.append(j)
    return result#ע���Ǻ����forѭ������

if __name__=="__main__":
    lst=[1,2,3,4]
    temp_result=permutation(lst)
    print temp_result


    