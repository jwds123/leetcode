# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
        """
        new_head = ListNode(-1)
        new_head.next = head
        pPreNode = new_head  # pPreNode：当前节点的前一个节点，需要始终与没有重复的节点相连

        while head and head.next:
            if head.val == head.next.val:
                #需要将重复元素连接起来
                pPreNode=head
                cur_val = head.val
                # 注意head不能为空
                while head and cur_val == head.val:
                    #cur=head
                    head = head.next
                #连接下一个非重复元素
                pPreNode.next = head
            else:
                pPreNode = head
                head = head.next
        return new_head.next

    def print_node(self,node):
        node_list=[]
        while node:
            node_list.append(str(node.val))
            node=node.next
        print('->'.join(node_list))

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(1)
    n4 = ListNode(2)
    n5 = ListNode(2)
    n6 = ListNode(3)
    n7 = ListNode(3)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    sol=Solution()
    sol.print_node(n1)
    n=sol.deleteDuplicates(n1)
    sol.print_node(n)