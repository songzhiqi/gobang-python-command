# -*- coding: utf-8 -*-
# 1) 功能区初始化
#
# 2) 打印棋盘
#
# 3) 打印胜利棋盘和赢家
#
# 4) 为控制台设置不同的字体的背景颜色
player = 1  # player有两个值1和-1，1代表*棋子，-1代表o
flag = "o"
y = 0
x = 0
finish = False


def vic():  # 3) 打印胜利棋盘和赢家函数
    print('    =============五子棋==============')  # 打印标题
    # 初始化棋盘
    print('    --------------------------------')
    print("       0  1  2  3  4  5  6  7  8  9")
    for i in range(len(checkerboard)):
        print("    " + chr(i + ord("A")) + " ", end=" ")
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ", end=" ")
        print()  # 打印棋盘
    print(
        '    --------------------------------  ')
    # 通过判断显示玩家胜利信息
    if player == 1:
        print('    *棋胜利，恭喜您，可真是五子棋小能手呀！   ')
    else:
        print('    o棋胜利，恭喜您，可真是五子棋小能手呀！    ')


# 最初的棋盘
print('    =============五子棋==============   ')  # 标题（五子棋）
# # 初始化棋盘
checkerboard = []  # 二维数组，用于打印棋盘
for i in range(10):  # 功能区初始化
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append("-")

# 打印棋盘
print('    --------------------------------')
print("       0  1  2  3  4  5  6  7  8  9")
for i in range(len(checkerboard)):
    print("    " + chr(i + ord("A")) + " ", end=" ")
    for j in range(len(checkerboard[i])):
        print(checkerboard[i][j] + " ", end=" ")
    print()  # 打印棋盘
print(
    '    --------------------------------   ')

# vic()

####下棋设置
# 1) 判断当前下棋的玩家
# 2) 记录棋子的位置
while True:
    player *= -1
    if player == -1:  # 判断当前下棋的玩家
        flag = "o"
        print('    请输入棋o的坐标位置（例如A1）：', end="")
    else:
        flag = "*"
        print('    请输入棋*的坐标位置（例如A1）：', end="")

        # 改变玩家

    # 输入棋子 chara
    while True:
        try:
            str = input()
            x = ord(str[0]) - 65
            y = int(str[1])
            break
        except:
            print("   你输入的有误请重新输入！ ", end="")
    if (x < 0 or x > 9 or y < 0 or y > 9):
        print('    你输入的有误请重新输入！         ', end="")
        continue
    if (checkerboard[x][y] == "-"):
        if player == 1:
            checkerboard[x][y] = "*"
        else:
            checkerboard[x][y] = "o"
    else:
        print('    你输入的位置有棋子，请重新添加！      ')
        continue

    # 打印棋盘
    print('    =============五子棋==============   ')  # 标题（五子棋）
    print('    --------------------------------')
    print("       0  1  2  3  4  5  6  7  8  9")
    for i in range(len(checkerboard)):
        print("    " + chr(i + ord("A")) + " ", end=" ")
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ", end=" ")
        print()  # 打印棋盘
    print(
        '    --------------------------------     ')

    # 2五子棋算法
    # 以一次棋子为中心
    # 八个方向的五个连续的棋子都为同一种颜色

    # 棋子的下侧
    if y - 4 >= 0 and y <= 9:  # 最左边要大于0，最右边的要小于9
        if (checkerboard[x][y - 1] == flag
                and checkerboard[x][y - 2] == flag
                and checkerboard[x][y - 3] == flag
                and checkerboard[x][y - 4] == flag):
            finish = True
            vic()
            break
    # 最后一个棋子在最后面
    # 棋子的上侧
    if y + 4 <= 9 and y >= 0:
        if (checkerboard[x][y + 1] == flag
                and checkerboard[x][y + 2] == flag
                and checkerboard[x][y + 3] == flag
                and checkerboard[x][y + 4] == flag):
            finish = True
            vic()
            break
    # 棋子的右侧
    if x + 4 <= 9 and x >= 0:
        if (checkerboard[x + 1][y] == flag
                and checkerboard[x + 2][y] == flag
                and checkerboard[x + 3][y] == flag
                and checkerboard[x + 4][y] == flag):
            finish = True
            vic()
            break
    # 棋子的左侧
    if x - 4 >= 0 and x <= 9:  # 下面的棋子的左侧的要大于0，最右面的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x - 1][y] == flag
                and checkerboard[x - 2][y] == flag
                and checkerboard[x - 3][y] == flag
                and checkerboard[x - 4][y] == flag):
            finish = True
            vic()
            break

    # 右下方
    if y - 4 >= 0 and y <= 9 and x + 4 <= 9 and x >= 0:  # 最左边要大于0，最右边的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y - 1] == flag
                and checkerboard[x + 2][y - 2] == flag
                and checkerboard[x + 3][y - 3] == flag
                and checkerboard[x + 4][y - 4] == flag):
            finish = True
            vic()
            break
    # 右上方
    if y + 4 <= 9 and y >= 0 and x + 4 <= 9 and x >= 0:  # 最左边要大于0，最右边的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y + 1] == flag
                and checkerboard[x + 2][y + 2] == flag
                and checkerboard[x + 3][y + 3] == flag
                and checkerboard[x + 4][y + 4] == flag):
            finish = True
            vic()
            break

    # 左下方
    if y - 4 >= 0 and y <= 9 and x - 4 >= 0 and x <= 9:  # 最 左下方 要大于0，最右上的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x - 1][y - 1] == flag
                and checkerboard[x - 2][y - 2] == flag
                and checkerboard[x - 3][y - 3] == flag
                and checkerboard[x - 4][y - 4] == flag):
            finish = True
            vic()
            break

    # 右下方
    if y - 4 >= 0 and y <= 9 and x + 4 <= 9 and x >= 0:  # 最 右下方要小于9，最左上方的要大于0
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y - 1] == flag
                and checkerboard[x + 2][y - 2] == flag
                and checkerboard[x + 3][y - 3] == flag
                and checkerboard[x + 4][y - 4] == flag):
            finish = True
            vic()
            break

    # 最后一个棋子在第一个或者第四个
    # 左边
    if y - 3 >= 0 and y + 1 <= 9:  # 最左边要大于0，最右边的要小于9
        if (checkerboard[x][y + 1] == flag
                and checkerboard[x][y - 1] == flag
                and checkerboard[x][y - 2] == flag
                and checkerboard[x][y - 3] == flag):
            finish = True
            vic()
            break

    # 棋子的上侧
    if y + 3 <= 9 and y - 1 >= 0:
        if (checkerboard[x][y + 1] == flag
                and checkerboard[x][y + 2] == flag
                and checkerboard[x][y + 3] == flag
                and checkerboard[x][y - 1] == flag):
            finish = True
            vic()
            break

    # 棋子的右侧
    if x + 3 <= 9 and x - 1 >= 0:
        if (checkerboard[x + 1][y] == flag
                and checkerboard[x + 2][y] == flag
                and checkerboard[x + 3][y] == flag
                and checkerboard[x - 1][y] == flag):
            finish = True
            vic()
            break
    # 棋子的左侧
    if x - 3 >= 0 and x + 1 <= 9:  # 下面的棋子的左侧的要大于0，最右面的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x - 1][y] == flag
                and checkerboard[x - 2][y] == flag
                and checkerboard[x - 3][y] == flag
                and checkerboard[x + 1][y] == flag):
            finish = True
            vic()
            break

    # 右下方
    if y - 3 >= 0 and y + 1 <= 9 and x + 3 <= 9 and x - 1 >= 0:  # 最左边要大于0，最右边的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y - 1] == flag
                and checkerboard[x + 2][y - 2] == flag
                and checkerboard[x + 3][y - 3] == flag
                and checkerboard[x - 1][y + 1] == flag):
            finish = True
            vic()
            break
    # 右上方
    if y + 3 <= 9 and y + 1 >= 0 and x + 3 <= 9 and x - 1 >= 0:  # 最左边要大于0，最右边的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y + 1] == flag
                and checkerboard[x + 2][y + 2] == flag
                and checkerboard[x + 3][y + 3] == flag
                and checkerboard[x - 1][y - 1] == flag):
            finish = True
            vic()
            break

    # 左下方
    if y - 3 >= 0 and y + 1 <= 9 and x - 3 >= 0 and x + 1 <= 9:  # 最 左下方 要大于0，最右上的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x - 1][y - 1] == flag
                and checkerboard[x - 2][y - 2] == flag
                and checkerboard[x - 3][y - 3] == flag
                and checkerboard[x + 1][y + 1] == flag):
            finish = True
            vic()
            break

    # 右下方
    if y - 3 >= 0 and y + 1 <= 9 and x + 3 <= 9 and x - 1 >= 0:  # 最 右下方要小于9，最左上方的要大于0
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y - 1] == flag
                and checkerboard[x + 2][y - 2] == flag
                and checkerboard[x + 3][y - 3] == flag
                and checkerboard[x - 1][y + 1] == flag):
            finish = True
            vic()
            break

    # 最后一个棋子在第2个或者第3个

    if y - 2 >= 0 and y + 2 <= 9:  # 最左边要大于0，最右边的要小于9
        if (checkerboard[x][y - 1] == flag
                and checkerboard[x][y - 2] == flag
                and checkerboard[x][y + 1] == flag
                and checkerboard[x][y + 2] == flag):
            finish = True
            vic()
            break

    # 棋子的上侧
    if y + 2 <= 9 and y - 2 >= 0:
        if (checkerboard[x][y + 1] == flag
                and checkerboard[x][y + 2] == flag
                and checkerboard[x][y - 1] == flag
                and checkerboard[x][y - 2] == flag):
            finish = True
            vic()
            break

    # 棋子的右侧
    if x + 2 <= 9 and x - 2 >= 0:
        if (checkerboard[x + 1][y] == flag
                and checkerboard[x + 2][y] == flag
                and checkerboard[x - 1][y] == flag
                and checkerboard[x - 2][y] == flag):
            finish = True
            vic()
            break
    # 棋子的左侧
    if x - 2 >= 0 and x + 2 <= 9:  # 下面的棋子的左侧的要大于0，最右面的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x - 1][y] == flag
                and checkerboard[x - 2][y] == flag
                and checkerboard[x + 1][y] == flag
                and checkerboard[x + 2][y] == flag):
            finish = True
            vic()
            break

    # 右下方
    if y - 2 >= 0 and y + 2 <= 9 and x + 2 <= 9 and x - 2 >= 0:  # 最左边要大于0，最右边的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y - 1] == flag
                and checkerboard[x + 2][y - 2] == flag
                and checkerboard[x + 3][y - 3] == flag
                and checkerboard[x + 4][y - 4] == flag):
            finish = True
            vic()
            break
    # 右上方
    if y + 2 <= 9 and y - 2 >= 0 and x + 2 <= 9 and x - 2 >= 0:  # 最左边要大于0，最右边的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y + 1] == flag
                and checkerboard[x + 2][y + 2] == flag
                and checkerboard[x - 1][y - 1] == flag
                and checkerboard[x - 2][y - 2] == flag):
            finish = True
            vic()
            break

    # 左下方
    if y - 2 >= 0 and y + 2 <= 9 and x - 2 >= 0 and x + 2 <= 9:  # 最 左下方 要大于0，最右上的要小于9
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x - 1][y - 1] == flag
                and checkerboard[x - 2][y - 2] == flag
                and checkerboard[x + 1][y + 1] == flag
                and checkerboard[x + 2][y + 2] == flag):
            finish = True
            vic()
            break

    # 右下方
    if y - 2 >= 0 and y + 2 <= 9 and x + 2 <= 9 and x + 2 >= 0:  # 最 右下方要小于9，最左上方的要大于0
        # y - 1 + i以最右边的棋子基准，看看是否都为同一个符号
        if (checkerboard[x + 1][y - 1] == flag
                and checkerboard[x + 2][y - 2] == flag
                and checkerboard[x - 1][y - 1] == flag
                and checkerboard[x - 2][y - 2] == flag):
            finish = True
            vic()
            break
