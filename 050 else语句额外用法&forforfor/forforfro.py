# -*- encoding: utf-8 -*-
"""
PyCharm forforfro
2022年06月01日
by littlefean
"""
from typing import *


# 如何跳出多层循环
# https://blog.csdn.net/m0_50973309/article/details/120990478
class getOutOfLoop(Exception):
    pass


def main():
    try:
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i == j == k == 1:
                        raise getOutOfLoop()  # 抛出一个异常，就会跳出所有循环
                    else:
                        print(i, j, k)
    except getOutOfLoop:

        pass
    print('done')
    return None


# python2.3
# 愚人节玩笑
# https://blog.csdn.net/shayuchaor/article/details/104071218?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-104071218-blog-120990478.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-104071218-blog-120990478.pc_relevant_paycolumn_v3&utm_relevant_index=5
# from goto import goto, label
#
# for i in range(9):
#     for j in range(9):
#         for k in range(9):
#             print("I am trapped, please rescue!")
#             if k == 2:
#                 goto.breakout  # 从多重循环中跳出
# label.breakout
# print("Freedom!")

def foo():
    def sub_foo():
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    print("I am trapped, please rescue!")
                    if k == 2:
                        return

    sub_foo()
    print("Freedom!")


foo()

#  。。。for else
for i in range(9):
    for j in range(9):
        for k in range(9):
            print("I am trapped, please rescue!")
            if k == 2:
                break
        else:
            continue
        break
    else:
        continue
    break
print("Freedom!")

# FLAG
...
...
...
...
...
...



if __name__ == "__main__":
    main()
