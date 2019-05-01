# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 18:10
# @Author  : Scavenger
# @FileName: 10  House Robber.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

def rob_recursion(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    if length == 0:
        return 0
    elif length == 2:
        return max(nums[0], nums[1])
    else:
        A = rob_recursion(nums[:length - 1])
        B = rob_recursion(nums[:length - 2]) + nums[-1]
        return max(A, B)


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    if length == 0:
        return 0
    memo = [-1 for i in range(length)]
    if length == 1:
        return nums[0]
    memo[0] = nums[0]
    memo[1] = max(nums[0], nums[1])
    for i in range(2, length):
        memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])
    return memo[-1]


if __name__ == "__main__":
    # lst = [1, 2, 3, 1]
    lst = [2, 7, 9, 3, 1]
    # lst = []
    num = rob_recursion(lst)
    num1 = rob(lst)
    print(num, num1)
