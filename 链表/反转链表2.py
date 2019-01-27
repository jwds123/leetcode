class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return
        if m==n:
            return head
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        stack[m-1:n]=reversed(stack[m-1:n])
        first=ListNode(0)
        new_head=first
        while stack:
            first.next=ListNode(stack.pop(0))#pop()最后一个元素 pop(0)第一个元素
            first=first.next
        return new_head.next

        # count = 1
        # root=ListNode(0)#head
        # root.next=head
        # pre=root#root的指针
        #
        # while pre.next and count < m:
        #     pre=pre.next
        #     count += 1
        # #print(pre.val)
        #
        # if count < m or m==n:
        #     return head
        #
        #
        # mNode=pre.next#第m个及以后的元素
        # cur=mNode.next#从第m+1个开始
        # #print(pre.val)
        # if cur.next==None:
        #     pre.next=cur
        #     cur.next=mNode
        # self.print_node(root.next)
        #
        # while cur.next and count < n:
        #     nextt = cur.next#先储存第i+1个元素
        #     cur.next = pre.next#反转：第i 个元素指向i-1个元素
        #     '''
        #     pre:正序的指针的next指向一直向下遍历的cur指针-pre.next
        #     pre.next:再下一个元素需要是倒序的
        #     '''
        #     pre.next = cur#pre：i-1个元素指向第i 个元素，第i 个元素指向i-1个元素,所以需要让第i个元素再指向第i+1个元素
        #     mNode.next = nextt#第i个元素再指向第i+1个元素
        #     cur = nextt#cur指针走向下一个元素
        #     count += 1
        #
        # return root.next

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
    n=sol.reverseBetween(n1,2,5)
    sol.print_node(n)