# author : 'wangzhong';
# date: 05/12/2020 23:53

"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
"""


class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class douleList:
    def __init__(self):
        # 伪头结点和伪尾节点
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeLast(self) -> Node:
        lastNode = self.tail.prev
        self.remove(lastNode)
        return lastNode

    def getSize(self) -> int:
        return self.size


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # 用作哈希
        self.hashMap = dict()
        # 双向链表，构成哈希双向链表
        self.cache = douleList()

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.put(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.hashMap:
            self.cache.remove(self.hashMap[key])
            self.cache.addFirst(newNode)
            self.hashMap[key] = newNode
        else:
            if self.cap == self.cache.getSize():
                lastNode = self.cache.removeLast()
                self.hashMap.pop(lastNode.key)
            self.cache.addFirst(newNode)
            self.hashMap[key] = newNode
