# 递归版本
def integerBreak_recursion(n):
    """
    :type n: int
    :rtype: int
    """
    memo = [-1 for i in range(n + 1)]
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    res = -1
    for i in range(1, n):
        res = max(res, i * (n - i), i * integerBreak_recursion(n - i))
        memo[i] = res
    return res


def integerBreak_dp(n):
    """
    :type n: int
    :rtype: int
    """
    memo = [-1 for i in range(n + 1)]
    memo[1] = 1
    res = -1
    for i in range(2, n + 1):
        for j in range(1, i):
            memo[i] = max(memo[i], j * (i - j), j * memo[i - j])
    return memo[-1]


# 动态规划版本

if __name__ == "__main__":
    # num = integerBreak_recursion(22)
    num = integerBreak_dp(22)
    print(num)
