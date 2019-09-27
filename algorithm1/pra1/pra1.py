#CODING=UTF-8
# 统计数字问题

file1 = open(".\算法1\算法实验1\input.txt","r")
n=int(file1.read())

Array = [0,0,0,0,0,0,0,0,0,0]
intArray = []
a=n
o=0
l=0
b=0

for x in Array:
    intArray.append(int(x))

for a in range(n):
    while(a%10!=0):
        b=int(a%10)
        intArray[b]=intArray[b]+1
        a=int(a/10)
    intArray[a%10]=intArray[b]+1

file1.close()

file2 = open(".\算法1\算法实验1\output.txt","w")


for x in intArray:
    x=str(x)
    file2.write(x + "\n")

file2.close()