def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid)

    arr = []
    for i in range(row):
        arr.append([])
        col = len(grid[i])
        for j in range(col):
            if i == 0 and j == 0:
                arr[i].append(grid[i][j])
            if i == 0 and j != 0:
                arr[i].append(arr[i][j - 1] + grid[i][j])
            if j == 0 and i != 0:
                arr[i].append(arr[i - 1][j] + grid[i][j])
            if i != 0 and j != 0:
                arr[i].append(grid[i][j] + min(arr[i][j - 1], arr[i - 1][j]))
    return arr[-1][-1]
    # return arr


if __name__ == "__main__":
    print(minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
