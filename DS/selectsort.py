# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 22:39
# @Author  : Scavenger
# @FileName: selectsort.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

def selectsort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j  # 全部走一遍，找到最小值的索引，再去交换
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == "__main__":
    lst = [3, 2, 4, 1, 8, 7]
    print(selectsort(lst))
