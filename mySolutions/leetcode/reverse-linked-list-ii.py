# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        node = ListNode(next=head)

        left_node = node
        
        for i in range(left-1):
            left_node = left_node.next

        curr = left_node.next
        prev = None
        for i in range(left, right+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        left_node.next.next, left_node.next = curr, prev

        return node.next
