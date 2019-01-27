class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        first=head
        stack=[]
        for i in range(len(lists)):
            while lists[i]:
                stack.append(lists[i].val)
                lists[i]=lists[i].next
        stack.sort()
        while stack:
            head.next=ListNode(stack.pop(0))
            head=head.next
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
    #n4.next = n5
    n5.next = n6
    n6.next = n7

    n11 = ListNode(8)
    n12 = ListNode(9)
    n13 = ListNode(10)
    n11.next = n12
    n12.next = n13
    sol = Solution()
    lists=[n1,n5,n11]
    sol.mergeKLists(lists)