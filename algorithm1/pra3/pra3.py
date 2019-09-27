#CODING=UTF-8
# 最多约数问题
first_int = 0
second_int = 0

file1 = open(".\算法实验3\input.txt","r")

first_int=int(file1.read(2).strip(" "))
second_int=int(file1.read(2).strip(" "))

file1.close()

# print(str(first_int)+" "+str(second_int))

app_Num = 0
app_Max = 0
num_Max = 0
second_int+=1
for n in range(first_int,second_int):
    for m in range(1,n):
        if ( n % m == 0):
            app_Num+=1
        else:
            pass
    if (app_Num > app_Max):
        app_Max = app_Num
        num_Max = n
    app_Num = 0

# print(num_Max)

file2 = open(".\算法实验3\output.txt","w")
file2.write(str(num_Max))
file2.close()