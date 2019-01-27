class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        K=k%len(stack)
        stack=stack[-K:]+stack[:-K]#最后两个与去除掉最后两个的列表
        head = h = ListNode(None)
        for i in stack:
            head.next = ListNode(i)
            head = head.next
        return h.next

if __name__ == '__main__':
    l=[1,2,3,4,5,6]
    print(l[-2:])#5，6
    print(l[:-2])#1，2，3，4
