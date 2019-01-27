class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        first=head
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next#指针往前走

        if l1!=None:
            head.next=l1
        if l2!=None:
            head.next=l2

        return first.next

    def print_node(self, node):
        node_list = []
        while node:
            node_list.append(str(node.val))
            node = node.next
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

    n11 = ListNode(8)
    n12 = ListNode(9)
    n13 = ListNode(10)
    n11.next = n12
    n12.next = n13
    sol = Solution()
    sol.print_node(n11)
    n=sol.mergeTwoLists(n1,n11)
    sol.print_node(n)

