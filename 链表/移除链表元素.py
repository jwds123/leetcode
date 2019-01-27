class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#删除链表中等于给定值 val 的所有节点。
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        pre=dummy
        while cur:
            if cur.val==val:
                pre.next=cur.next
            else:
                pre=pre.next
            cur=cur.next
        return dummy.next
