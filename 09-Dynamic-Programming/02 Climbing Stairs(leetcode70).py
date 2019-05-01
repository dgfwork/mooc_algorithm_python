def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    lst = []
    lst.append(0)  # 占住索引为0的位置
    lst.append(1)  # n=1 一种办法
    lst.append(2)  # n=2 两种办法
    for i in range(3, n + 1):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[-1]


if __name__ == "__main__":
    num = climbStairs(1)
    print(num)
