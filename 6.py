# coding:utf-8

# 单链表的实现
# class Lnode:
#     def __init__(self, elem, next_=None):
#         self.elem = elem
#         self.next = next_
# # 构建链表
#
# head = Lnode(1)
# p = Lnode(1)
# for i in xrange(2,11):
#     p.next = Lnode(i)
#     p = p.next
#
# while head:
#     print head.elem
#     head = head.next


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

# 单链表的一个实现函数
listnode = ListNode(1)
p = listnode
for i in xrange(2,11):
    listnode.next = ListNode(i)
    listnode = listnode.next
while p:
    print p.val
    p = p.next

# 利用栈
class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode.val is None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l




s = Solution()
print s.printListFromTailToHead(p)
#
# '''
# 输入一个链表，从尾到头打印链表每个节点的值。
# '''
#
#
# class ListNode:
#     def __init__(self, x=None):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def printListFromTailToHead(self, listNode):
#         if listNode.val == None:
#             return
#         l = []
#         head = listNode
#         while head:
#             l.insert(0, head.val)
#             head = head.next
#         return l
#
#
# node1 = ListNode(10)
# node2 = ListNode(11)
# node3 = ListNode(13)
# node1.next = node2
# node2.next = node3
#
# singleNode = ListNode(12)
#
# test = ListNode()
#
# S = Solution()
# print(S.printListFromTailToHead(node1))
# print(S.printListFromTailToHead(test))
# print(S.printListFromTailToHead(singleNode))
