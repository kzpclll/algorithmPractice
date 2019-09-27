#CODING=UTF-8
import gloabl_var_model as gl
import random

#  boardArray1:棋盘
#  sx:特殊棋格的x坐标 sy:特殊棋格的y坐标
#  bx:该部分棋盘在数组中的x坐标 by:同上y坐标
#  size:当前部分棋盘的边长 一定是2的倍数 
def ChessBoard (boardArray1,sx,sy,bx,by,size):
    # 检验是否分完
    if (size == 1):
        return 
    # t为当前骨牌编号
    gl.gl_int_i+=1
    t = gl.gl_int_i
    s = int(size/2)

    # 检验当前四分棋盘的左上角是否有特殊棋格
    if (sx<bx+s and sy<by+s):
        ChessBoard(boardArray1,sx,sy,bx,by,s)
    else:
        # 给左上角棋盘的右下角增加一个当前编号的棋格
        boardArray1[bx+s-1][by+s-1] = t
        ChessBoard(boardArray1,bx+s-1,by+s-1,bx,by,s)

    # 检验右上角棋盘
    if(bx+s<=sx and sy<(by+s)):
        ChessBoard(boardArray1,sx,sy,bx+s,by,s)
    else:
        # 右上角棋格对应的是左下角
        boardArray1[bx+s][by+s-1] = t
        ChessBoard(boardArray1,bx+s,by+s-1,bx+s,by,s)

    # 检验左下棋盘
    if(sx<(bx+s) and by+s<=sy):
        ChessBoard(boardArray1,sx,sy,bx,by+s,s)
    else:
        boardArray1[bx+s-1][by+s] = t
        ChessBoard(boardArray1,bx+s-1,by+s,bx,by+s,s)

    # 最后检验右下棋盘
    if(bx+s<=sx and by+s<=sy):
        ChessBoard(boardArray1,sx,sy,bx+s,by+s,s)
    else:
        boardArray1[bx+s][by+s] = t
        ChessBoard(boardArray1,bx+s,by+s,bx+s,by+s,s)
#------------------------------------------------------------------------------ 
def showBoard (boardArray1):
    print("生成的棋盘如下:")
    for x in range(i_size):
        for y in range(i_size):
            print(boardArray1[x][y],end=" ")
        print("")

# ---------------------------------------------------------------------------
# 提示和输入
print("输入棋盘的size:")
i_size = int(input())
# 简单粗暴的合格数数列
int_List1 = [4,8,16,64]
# 边际检验
bIsOk = False
while (bIsOk == False):

    for x in int_List1:
        if(i_size == x):
            bIsOk = True
            break

    if (bIsOk == False):
        print("输入的数不为4的n次方形式或者过大不方便显示,请重新输入:")
        i_size = int(input())

    

# 按照输入创建二维数组棋盘
boardArray = [[0 for i in range(i_size)] for j in range(i_size)]

# 随机生成特殊棋盘
i_sx = int(random.randrange(0,i_size))
i_sy = int(random.randrange(0,i_size))
boardArray[i_sx][i_sy] = "x" 
print("随机特殊棋格位置为:[" + str(i_sx) + "][" + str(i_sy) + "]")
# 定义用于找到棋盘初始位置的x，y变量
i_x = 0
i_y = 0
# 初始化静态变量
gl.gl_int_i = 0
# 进入递归
ChessBoard(boardArray,i_sx,i_sy,i_x,i_y,i_size)
showBoard(boardArray)