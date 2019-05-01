def fib_recursion(num):
    # f(1)=1 f(2)=1
    if num == 1 or num == 2:
        return 1
    else:
        # f(n) = f(n-1)+f(n-2)
        return fib_recursion(num - 1) + fib_recursion(num - 2)


def fib_dp(num):
    lst = []
    lst.append(0)  # 将下标0的位置占住
    lst.append(1)  # f(1) = 1
    lst.append(1)  # f(2) = 1
    for i in range(3, num + 1):
        # f(n) = f(n-1) + f(n-2)
        lst.append(lst[i - 1] + lst[i - 2])

    return lst[len(lst) - 1]


if __name__ == "__main__":
    num1 = fib_recursion(10)
    num2 = fib_dp(10)
    print(num1, num2)
