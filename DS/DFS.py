# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 9:42
# @Author  : Scavenger
# @FileName: DFS.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

def DFS(graph, start):
    queue = []
    queue.append(start)
    memo = set()  # 小本本记录是否访问过
    memo.add(start)
    while queue:
        temp = queue.pop()  # 后进先出  栈
        print(temp, end=" ")
        lst = graph.get(temp)  # 获取到邻接点
        for item in lst:
            if item not in memo:  # 不在小本本上面的话 加入小本本 再入队列
                memo.add(item)
                queue.append(item)


if __name__ == "__main__":
    graph = {
        "A": ["B", "D", "E"],
        "B": ['A', 'E', 'C'],
        "C": ['B', 'E', 'F'],
        "D": ['A', 'E'],
        "E": ['A', 'B', 'C', 'D'],
        'F': ['C']
    }
    DFS(graph, "F")
