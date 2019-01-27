# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#请编写一个函数，使其可以删除某个链表中给定的（非末尾的）节点，您将只被给予要求被删除的节点。
class Solution(object):
    def deleteNode(self, node):
        """
        输入: head = [4,5,1,9], node = 5
        输出: [4,1,9]
        解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
        """
        if node == None:
            return node

        if node.next == None:
            node = None

        node.val=node.next.val#当前值被后一个值覆盖
        node.next=node.next.next#下一节点跳到下下一节点

    def print_node(self,node):
        node_list=[]
        while node:
            node_list.append(str(node.val))
            node=node.next
        print('->'.join(node_list))

if __name__ == '__main__':
    pHead=Node(90)
    node2=Node(34)
    node3=Node(89)
    node4=Node(77)
    node5=Node(23)
    pHead.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    sol=Solution()
    sol.print_node(pHead)
    sol.deleteNode(node3)
    sol.print_node(pHead)

