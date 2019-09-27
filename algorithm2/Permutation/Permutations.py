# CODING=UTF-8
# 全排列问题(无重复数字情况)
# ---------------------------------------------------
# num_perm: 当前轮次用于排序的数字总数  num_last: 整个列表的最大值
def Perm(num_perm,num_last):
    #假如已排序总数等于列表的最大值 则说明只剩最后一个数字 没有再排序的必要 直接输出
    if(num_perm == num_last):
        print(intArray1)
    else: 
        # 有多少个数字参与排序本轮就有多少次循环
        for n in range(num_perm+1):
            Swap(n,num_perm)
            # 进入下一轮
            Perm(num_perm+1,num_last)
            # 复原数列
            Swap(n,num_perm)

#---------------------------------------------------
def Swap (num_1,num_2):

    i_temp = intArray1[num_1]
    intArray1[num_1] = intArray1[num_2]
    intArray1[num_2] = i_temp  

intArray1 = []
print("输入排序数组(输入-1时终止输入):")

i_num = int(input())
while(i_num!=-1):
    intArray1.append(i_num)
    i_num = int(input())
print("得到数组:",intArray1)

Perm(1,len(intArray1))


