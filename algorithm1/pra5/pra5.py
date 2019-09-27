#CODING=UTF-8
# fibonacci数列 (非优解)


# i_Temp = 当前的数列次序 n = 目标次序
# num1 = 前二位数字 num2 = 前一位数字 
def typeFibonacci (num1,num2,i_Temp,i_Aim):  
    # print("成功进入函数.....")   
    n = 0

    if(i_Aim == 1):
        return 1

    if(i_Temp==1):
        num1 = 1
        num2 = 0

    if(i_Temp==2):
        num1 = 1
        num2 = 1

    if(i_Temp>=3):
        n = num2
        num2 = num1 + num2
        num1 = n

    # print("检测数列:")
    # print(num1,num2)

    if(i_Temp==i_Aim):
        # print("正常结束分支")
        return num2
    elif (i_Temp<i_Aim):
        i_Temp+=1
        # print("进入循环分支")
        return typeFibonacci(num1,num2,i_Temp,i_Aim)
    else:
        # print("溢出分支")
        print("out of range")
        return 0

i_Temp = 1
n = 110
num1 = 0
num2 = 0
print(typeFibonacci(num1,num2,i_Temp,n))







