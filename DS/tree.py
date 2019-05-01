# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 19:16
# @Author  : Scavenger
# @FileName: tree.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.rchild = None
        self.lchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = Node
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)


if __name__ == "__main__":
    tree = Tree()
