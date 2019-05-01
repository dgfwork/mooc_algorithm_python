def minimumTotal_recursion(triangle):
    # 里面的参数是二维数组
    dd = float("inf")  # 无穷大
    row = len(triangle)
    arr = []
    for i in range(row):
        col = len(triangle[i])
        arr.append([])
        for j in range(col):
            if i == 0 and j == 0:
                num1 = 0
                num2 = 0
            else:
                # try:
                #     num1 = arr[i - 1][j - 1]  # 负索引
                #     print("try", num1)
                # except:
                #     num1 = dd
                #     print("except", num1)
                if j < 1:
                    num1 = dd
                else:
                    num1 = arr[i - 1][j - 1]
                try:
                    num2 = arr[i - 1][j]
                except:
                    num2 = dd
            # print("i=", i, "j=", j, "当前数字为triangle[i][j]", triangle[i][j], ",", num1, num2)

            arr[i].append(triangle[i][j] + min(num1, num2))
            # print(arr[i], triangle[i][j], min(num1, num2))
    return min(arr[-1])


# 动态规划
if __name__ == "__main__":
    # 为什么会这样？ 每一行的两端都应该有个inf才是正常的 .list里面有负索引 捕获不到异常
    # print(minimumTotal_recursion([[-1], [3, 2], [-3, 1, -1]]))
    print(minimumTotal_recursion([[2], [3, 4], [6, 5, 7]]))
