# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy=ListNode(0)
        pre=dummy
        first=head
        second=head.next
        while second:
            pre.next=second
            first.next=second.next
            second.next=first

            pre=first
            first=first.next
            second=first.next if first else None
        return dummy.next

    def print_node(self,node):
        node_list=[]
        while node:
            node_list.append(str(node.val))
            node=node.next
        print('->'.join(node_list))

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    n11=ListNode(3)
    n12=ListNode(4)
    n13=ListNode(5)
    n11.next=n12
    n12.next=n13
    sol=Solution()
    sol.print_node(n1)
    n=sol.swapPairs(n1)
    sol.print_node(n)
