# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 18:55
# @Author  : Scavenger
# @FileName: hanoi.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

count = 0


def hanoi(level, A, B, C):
    global count
    if level == 1:
        count += 1
        print("%s->%s" % (A, C))
    else:
        # 递归的时候 现将上面的level-1个经过C移动到B
        hanoi(level - 1, A, C, B)
        # 再将最大的一个盘子移动到C
        count += 1
        print("%s->%s" % (A, C))
        hanoi(level - 1, B, A, C)


if __name__ == "__main__":
    hanoi(3, "A", "B", "C")
    print("需要移动的次数为:", count)
