# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 9:52
# @Author  : Scavenger
# @FileName: singlinklist.py
# @Software: PyCharm
# @Github  : https://github.com/dgfwork/
# @Blog    : https://www.cnblogs.com/gaofeng-d/

class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val


class SingLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        """
        :return:链表长度
        """
        if self.is_empty():
            return 0
        else:
            cur = self.__head
            count = 0
            while cur:
                count += 1
                cur = cur.next
        return count

    def append(self, val):  # 尾插法
        node = Node(val)
        if self.__head == None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next  # 找到尾结点
            cur.next = node

    def travel(self):
        if self.is_empty():
            return
        else:
            cur = self.__head
            while cur:
                print(cur.val, end=" ")
                cur = cur.next

    def add(self, val):
        """
         头插法  画表示意即可
        :param val:插入值
        :return:
        """
        node = Node(val)
        node.next = self.__head
        self.__head = node

    def insert(self, position, value):
        if position <= 0:
            position = 0
        if position >= self.length() - 1:
            position = self.length() - 1
        # 插入位置正常之后，找到位置插入进去即可
        pre = self.__head
        count = 0
        node = Node(value)
        while count < position - 1:
            count += 1
            pre = pre.next
        node.next = pre.next
        pre.next = node

    def remove(self, item):
        pre = self.__head
        # 要遍历到需要删除节点的前一个节点
        while pre.next:
            # 这里面还需要对删除第一个元素做单独处理
            if item == pre.val:
                self.__head = pre.next
                break
            else:
                # 处理中间和后面的元素
                if pre.next.val == item:
                    pre.next = pre.next.next
                else:
                    pre = pre.next

    def search(self, item):
        """
        全部遍历一遍
        :param item:
        :return:
        """
        cur = self.__head
        while cur:
            if cur.val == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    sll = SingLinkList()
    sll.append(100)
    sll.append(200)
    sll.append(300)
    sll.append(400)
    sll.add(10)
    sll.add(20)
    sll.travel()
    print(" ")
    print(sll.length())
    sll.remove(200)
    sll.travel()
