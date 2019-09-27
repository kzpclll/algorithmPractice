#CODING=UTF-8
# 字典编码问题
def getBaseCode (n,num):
    if(n>1):
        num += num * 26
        n-=1
        return getBaseCode(n,num)
    else:
        return num


file1 = open(".\算法实验2\input.txt","r")
list1=""
n=int(file1.readline())
chararray = []
for x in range(n):
    list1 = file1.readline()
    list1 = list1.strip('\n')
    chararray.append(list1)
file1.close()
num = 1

print(chararray)
print(getBaseCode(n,num))

num = getBaseCode(n,num)

i_Temp = 0
ch_Temp = ""
for x in range(n):
    ch_Temp = chararray[-x]
    i_Temp = ord(ch_Temp)
    num += ( i_Temp - (96+n-x) ) * getBaseCode(x,1) 
print(num)
num = str(num)
file2 = open(".\算法实验2\output.txt","w")
file2.write(num)
file2.close()