# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 21:24
# @Author  : Scavenger
# @FileName: bubblesort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

def bubblesort(nums):
    n = len(nums)
    for i in range(n - 1):
        # 第一层表示需要排这么多趟
        change_flag = False
        for j in range(n - 1 - i):
            # 第二层里面的长度是动态的
            if nums[j] > nums[j + 1]:
                change_flag = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # 优化一下有序的情况
        if not change_flag:
            break
    return nums


if __name__ == "__main__":
    lst = bubblesort([3, 2, 4, 1, 8, 7])
    print(lst)
