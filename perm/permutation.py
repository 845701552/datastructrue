#coding: utf-8

"""
python实现全排列
"""
def permutation(lst):
    """
    python使用递归实现全排列
    """
    if len(lst)==0 or len(lst)==1:
        return [lst]
    result=[]
    for i in lst:
        temp_list=lst[:]#将lst数组赋值给temp_list
        temp_list.remove(i)#删除
        temp=permutation(temp_list)#递归生成删除一个元素后的全排列
        for j in temp:#遍历生成的全排列
            j.insert(0,i)#将删除的i添加到最前面
            result.append(j)
    return result#注意是和外层for循环对齐

if __name__=="__main__":
    lst=[1,2,3,4]
    temp_result=permutation(lst)
    print temp_result


    