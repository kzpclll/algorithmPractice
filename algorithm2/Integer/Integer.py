#CODING=UTF-8
# 整数划分问题

print("输入要划分的整数:")

i_Num = int(input())
i_Temp = i_Num

def IntSpirate (n,m):
    n = int(n)
    m = int(m)

    if (n==1 or m==1):
        return 1

    if (n<m):
        return IntSpirate (n,n)

    if (n==m):
        return 1 + IntSpirate (n,m-1)    

    if (n>m):
        return IntSpirate(n,m-1) + IntSpirate(n-m,m)
    
print("一共有",IntSpirate(i_Temp,i_Num),"种整数分割方式")

