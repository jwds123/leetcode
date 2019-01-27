class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        stack=[]
        new_head=ListNode(-1)
        pre_head=head
        p=new_head
        while head:
            stack.append(head.val)
            head=head.next

        if len(stack)<k:
            return pre_head

        n=len(stack)//k
        for i in range(n):
            stack[i*k:(i+1)*k]=reversed(stack[i*k:(i+1)*k])

        while stack:
            p.next=ListNode(stack.pop(0))
            p=p.next
        return new_head.next

    def reverseKGroup1(self, head, k):
        current_node = head
        count_node = 0
        while current_node and count_node != k:
            current_node = current_node.next
            count_node += 1
        # if current_node:
        #     print(current_node.val)

        if count_node == k:
            current_node = self.reverseKGroup1(current_node, k)
            #print(current_node.val)

            while count_node > 0:
                temp_node = head.next
                #print(temp_node.val)
                head.next = current_node
                #print(current_node.val)
                current_node = head
                head = temp_node
                count_node -= 1
            head = current_node
        self.print_node(current_node)
        return head


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

    n11 = ListNode(3)
    n12 = ListNode(4)
    n13 = ListNode(5)
    n11.next = n12
    n12.next = n13
    sol = Solution()
    sol.print_node(n1)
    n=sol.reverseKGroup1(n1,3)
    sol.print_node(n)

