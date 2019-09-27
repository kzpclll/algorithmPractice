#CODING=UTF-8
# 桶排序 最大间隙问题
floatArray=[]
i_num = 0

file1 = open(".\算法实验4\input.txt","r")

i_num=int(file1.read(2).strip("\n"))
for x in range(i_num):
    floatArray.append(float(file1.read(4).strip(" ")))

file1.close()

print("数字数量:")
print(i_num)
print("得到的数字[1-10]:")
print(floatArray)

bucketList = [[0 for i in range(2)] for i in range(10)]
print("数组初始化:")
print(bucketList)

for x in range(10):
    bucketList[x][1] = 10

i_Temp = 0
# bucketList[n][0]为桶中的最大值
# bucketList[n][1]为桶中的最小值
for x in range(i_num):
    i_Temp = int(floatArray[x])
    if(bucketList[i_Temp][0] < floatArray[x]):
        bucketList[i_Temp][0] = floatArray[x]
    else:
        pass
    
    if(bucketList[i_Temp][1] > floatArray[x]):
        bucketList[i_Temp][1] = floatArray[x]
    else:
        pass

print("桶排序完成:")    
print(bucketList)

farestDistance = 0

for m in range(10):
    if(bucketList[m][0]!=0):
        for n in range (m+1,10):
            if(bucketList[n][0]!=0):
                if(farestDistance<bucketList[n][0]-bucketList[m][1]):
                    farestDistance = bucketList[n][0]-bucketList[m][1]
                    break
                else:
                    break
            else:
                pass

print("找到的最大距离是:")
print(farestDistance)

file2 = open(".\算法实验4\output.txt","w")
file2.write(str(farestDistance))
file2.close()